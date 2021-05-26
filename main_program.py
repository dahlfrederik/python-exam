import sys
import modules.regression as regression

import pandas as pd

# import module that returns a dataframe
# IMPORTANT !!
#

# Should be values returned from webscraping module
d = {'name': ["Tesla Model S 85 5d", "Tesla Model S 75D 5d"],
     'km': [141000, 36000], "price": [299700, 589900], "year": [2014, 2019]}
df = pd.DataFrame(data=d)
search_car_km = 93000
search_car_year = 2010
##
find_car = regression.find_car_value(
    df, search_car_km, search_car_year)

find_car.show_dataframe()
find_car.normalize_data()
find_car.describe_data()
find_car.train_model()
find_car.show_coff_and_interception()
find_car.prediction_vs_real()
find_car.predict_car_value()
