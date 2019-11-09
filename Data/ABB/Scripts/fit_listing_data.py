# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 17:39:51 2019

@author: BolesMi
"""

# import packages
import pandas as pd
import statsmodels.formula.api as smf

# import cleaned SF listing dataset
listings_sf_clean = pd.read_csv('.\Data\Clean\San_Francisco\listings_sf_data_clean.csv')

# encode categorical variables in new dataframe
listings_sf_1 = listings_sf_clean.copy()
listings_sf_2 = pd.get_dummies(listings_sf_1, columns=['neighbourhood','property_type','room_type'], prefix=['neighborhood','prop_type','room_type'])

# get column names
listings_sf_2_colnames = listings_sf_2.columns.tolist()

### sklearn ###

# set features (independent) and labels (dependent)
X = listings_sf_2.drop(['id','name','host_name','latitude','longitude','square_feet',
                        'availability_30','availability_90','availability_365','last_review'], axis=1)
y = listings_sf_2['monthly_revenue']

# fit data
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, y)
#regressor.intercept_, regressor.coef_

# predict values based on model
y_pred = regressor.predict(x) # listing + surroundings data
y_pred2 = regressor.predict(x2) # listing data only

# calculate difference between predicted and actual prices
diff = round((y - y_pred2), 6)





# build model from data using backward elimination
formula_1 = 'monthly_revenue ~ bedrooms + bathrooms + guests_included + number_of_reviews + guests_included + '


regressor = smf.ols(formula_1, data = listings_sf_2).fit() # settled on formula_3
regressor.summary()
summary = regressor.summary()
summary_text = summary.as_text()

