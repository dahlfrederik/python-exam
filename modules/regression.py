

import pandas as pd
import sklearn.linear_model
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np


class find_car_value:
    def __init__(self, dataframe, search_car_km, search_car_year):
        self.dataframe = dataframe
        self.regressor = LinearRegression()
        # Setting X (km and year) and Y (price)
        self.X = self.dataframe[['km', 'year']]
        self.y = self.dataframe['price']
        self.search_car_km = search_car_km
        self.search_car_year = search_car_year
        self.y_test = []
        self.y_pred = []

    def get_x_y(self):
        return self.X, self.y

    def show_dataframe(self):
        return self.dataframe.head()

    def normalize_data(self):
        # Defining features
        features = self.dataframe[['km', 'year', 'price']]
        # Normalize data (reduce values to be between 0 and 1)
        scaler = preprocessing.MinMaxScaler()
        names = features.columns
        d = scaler.fit_transform(features)
        scaled_df = pd.DataFrame(d, columns=names)
        return scaled_df

    def describe_data(self):
        return self.dataframe.describe()

    def train_model(self):
        # Dividing data into training and test sets
        X_train, X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=0)
        # Training the model
        self.regressor.fit(X_train, self.y_train)
        return X_test, self.y_test

    def show_coff_and_interception(self):
        coeff_df = pd.DataFrame(
            self.regressor.coef_, self.X.columns, columns=['Coefficient'])
        intercept = self.regressor.intercept_
        return coeff_df, intercept

    def prediction_vs_real(self):
        X_test, y_test = find_car_value.train_model(self)
        y_pred = self.regressor.predict(X_test)
        df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
        return df

    def predict_car_value(self):
        # Predicting result based on car values
        predicted_car_value = self.regressor.predict(
            [[int(self.search_car_km), int(self.search_car_year)]])
        print(f"Value of the entered car: {str(predicted_car_value)[1:-1]} kr")

    def predict_data_accuracy(self):
        accuracy = (self.regressor.score(self.X, self.y))*100
        print(f"Model accuracy: {accuracy} %")
