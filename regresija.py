import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, root_mean_squared_error
import seaborn as sns


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

    return grid_search.best_params_


def main():
    X_train, X_test, y_train, y_test = duomenys_modeliams('nt_data_fin_iki500K.csv')
    best_hyper_params_rf(X_train, y_train)

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

    #  Train and evaluate models using cross-validation
    linear_reg_scores = cross_val_score(linear_reg_model, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
    rf_scores = cross_val_score(rf_model, X_train, y_train, cv=5, scoring='neg_mean_squared_error')

    # Convert mean squared error scores to positive values
    linear_reg_rmse_scores = (-linear_reg_scores) ** 0.5
    rf_rmse_scores = (-rf_scores) ** 0.5

    # Print the cross-validated RMSE scores
    print("Linear Regression Cross-Validated RMSE Scores:", linear_reg_rmse_scores)
    print("Random Forest Cross-Validated RMSE Scores:", rf_rmse_scores)

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


if __name__ == '__main__':
    main()
