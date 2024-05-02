import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, KFold
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, root_mean_squared_error
import seaborn as sns
from dash import Dash, html, dcc
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate
import plotly.express as px



def duomenys_modeliams(failas):
    # Selecting columns from the DataFrame
    df = pd.read_csv(failas)
    df = df.drop('No', axis=1)
    X = df.drop('Price', axis=1)
    y = df['Price']

    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.3, random_state=101)
    return X_train, X_test, y_train, y_test


def best_hyper_params_rf(X_train, y_train):
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 10, 20],
    }
    grid_search = GridSearchCV(estimator=RandomForestRegressor(random_state=101),
                               param_grid=param_grid,
                               cv=5,
                               scoring='neg_mean_squared_error',
                               n_jobs=-1)

    grid_search.fit(X_train, y_train)
    print('Best Hyperparameters for Random Forest:', grid_search.best_params_)
    print('Best Result:', grid_search.best_score_)
    return None

def regresijos(X_train, X_test, y_train, y_test):
    # Initialize regression models
    linear_reg_model = LinearRegression()
    rf_model = RandomForestRegressor(n_estimators=300, max_depth=10, random_state=101)

    # Train the models on the entire training set and evaluate on the test set
    linear_reg_model.fit(X_train, y_train)
    rf_model.fit(X_train, y_train)

    linear_reg_pred = linear_reg_model.predict(X_test)
    rf_pred = rf_model.predict(X_test)

    linear_reg_rmse = root_mean_squared_error(y_test, linear_reg_pred)
    rf_rmse = root_mean_squared_error(y_test, rf_pred)
    print(f"Linear Regression RMSE: {linear_reg_rmse:.2f}")
    print(f"Random Forest Test RMSE: {rf_rmse:.2f}")

    linear_reg_r2 = r2_score(y_test, linear_reg_pred)
    rf_r2 = r2_score(y_test, rf_pred)
    print(f'Linear Regression r2 = {linear_reg_r2:.2f}')
    print(f'Random Forest r2 = {rf_r2:.2f}')

    #  Evaluate models using cross-validation
    folds = KFold(n_splits=5, shuffle=True, random_state=101)
    linear_reg_scores = cross_val_score(linear_reg_model, X_train, y_train, cv=folds, scoring='r2')
    rf_scores = cross_val_score(rf_model, X_train, y_train, cv=folds, scoring='r2')

    # Print the cross-validated RMSE scores
    print("Linear Regression Cross-Validated r2 scores:", linear_reg_scores)
    print("Random Forest Cross-Validated r2 scores:", rf_scores)

    # Test vs Predicted Prices Visualization
    plt.figure(figsize=(12, 6))
    plt.scatter(y_test, linear_reg_pred, label='Linear Regression')
    plt.scatter(y_test, rf_pred, label='Random Forest')
    plt.plot(y_test, y_test, 'r')
    plt.title('Test vs Predicted Price')
    plt.xlabel('Test Price')
    plt.ylabel('Predicted Price')
    plt.xlim(0, 500000)
    plt.ylim(0, 500000)
    plt.legend()
    plt.show()

    # Features Importance Visualization
    feature_importances = pd.Series(rf_model.feature_importances_, index=X_train.columns).sort_values(ascending=False)
    plt.figure(figsize=(14, 6))
    sns.barplot(x=feature_importances, y=feature_importances.index)
    plt.title('Features Importance using Random Forest')
    plt.xlabel('Importance Level')
    plt.ylabel('Features')
    plt.show()
    return y_test, linear_reg_pred, rf_pred

def nt_plotly(y_test, linear_reg_pred, rf_pred):

    # Preparing data for visualisation
    test_linear = pd.DataFrame({'Test price': y_test, 'Predicted price': linear_reg_pred})
    test_rf_df = pd.DataFrame({'Test price': y_test, 'Predicted price': rf_pred})
    test_linear['Model'] = 'Linear Regression'
    test_rf_df['Model'] = 'Random Forest Regression'
    model_df = pd.concat([test_linear, test_rf_df], axis=0)

    # Visualisation using Plotly
    app = Dash(__name__)

    app.layout = html.Div([
        html.H2('Linear Regression and Random Forest Visualization \n'),
        html.H4('Please select the model for visualisation: \n'),
        dcc.Dropdown(
            id='model-id',
            options=list(model_df['Model'].unique()),
            value='Linear Regression',
            style={"width": "70%"}
        ),
        dcc.Graph(id='visual-output')
    ])

    @app.callback(
        Output('visual-output', 'figure'),
        Input('model-id', 'value')
    )
    def model_visualisation(model_name):
        figure = px.scatter(
            model_df.query(f"Model == '{model_name}'"),
            x='Test price',
            y='Predicted price',
            title=f'{model_name}. Test vs Predicted Price'
        ).update_layout(
            title_font=dict(color='blue', size=16),
            title={
                'x': 0.5,
                'y': 0.9,
                'xanchor': 'center'
            },
            width=800,
            height=600
        )

        figure.update_xaxes(title='Test price', range=[0, 510000])
        figure.update_yaxes(title='Predicted price', range=[0, 510000])
        return figure

    app.run_server(port=8060)


def main():
    X_train, X_test, y_train, y_test = duomenys_modeliams('nt_data_fin_iki500K.csv')
    # best_hyper_params_rf(X_train, y_train)
    y_test, linear_reg_pred, rf_pred = regresijos(X_train, X_test, y_train, y_test)
    nt_plotly(y_test, linear_reg_pred, rf_pred)

if __name__ == '__main__':
    main()
