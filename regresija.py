import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def duomenu_parengimas_modeliui(failas):
    # Selecting columns from the DataFrame
    df = pd.read_csv(failas)
    df = df[['Price', 'House area', 'Rooms No.', 'Floors', 'Year of construction', 'Land area (a)']]

    # Ensure numeric values for 'Rooms No.' and 'Floors'
    df['Rooms No.'] = pd.to_numeric(df['Rooms No.'], errors='coerce').astype(float)
    df['Floors'] = pd.to_numeric(df['Floors'], errors='coerce').astype(float)

    # Drop rows with NaN values
    df = df.dropna()

    return df

def main():
    failas = 'nt_data_fin.csv'
    df = duomenu_parengimas_modeliui(failas)
    X = df.drop('Price', axis=1)
    y = df['Price']

    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize regression models
    linear_reg_model = LinearRegression()
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

    # Train and evaluate models using cross-validation
    linear_reg_scores = cross_val_score(linear_reg_model, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
    rf_scores = cross_val_score(rf_model, X_train, y_train, cv=5, scoring='neg_mean_squared_error')

    # Convert mean squared error scores to positive values
    linear_reg_rmse_scores = (-linear_reg_scores)**0.5
    rf_rmse_scores = (-rf_scores)**0.5

    # Print the cross-validated RMSE scores
    print("Linear Regression Cross-Validated RMSE Scores:", linear_reg_rmse_scores)
    print("Random Forest Cross-Validated RMSE Scores:", rf_rmse_scores)

    # Train the models on the entire training set and evaluate on the test set
    linear_reg_model.fit(X_train, y_train)
    rf_model.fit(X_train, y_train)

    linear_reg_pred = linear_reg_model.predict(X_test)
    rf_pred = rf_model.predict(X_test)

    linear_reg_rmse = mean_squared_error(y_test, linear_reg_pred, squared=False)
    rf_rmse = mean_squared_error(y_test, rf_pred, squared=False)

    print(f"Linear Regression Test RMSE: {linear_reg_rmse:.2f}")
    print(f"Random Forest Test RMSE: {rf_rmse:.2f}")

    plt.scatter(y_test, linear_reg_pred, label='Linear Regression')
    plt.scatter(y_test, rf_pred, label='Random Forest')
    plt.xlabel('True Price')
    plt.ylabel('Predicted Price')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()