# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:31:23 2019

@author: michaelboles
"""

# set up working directory
import os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
#os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import master dataset    
import pandas as pd
data_all = pd.read_csv('./data/data_clean.csv')

# remove zeros, NaNs, index column
data_temp2 = data_all.dropna()
data_clean = data_temp2[(data_temp2 != 0).all(1)]

# select only Bay Area
data_bay = data_clean.query('-122.7 < Longitude < -121.5 and 37.15 < Latitude < 38.15')

# select only columns for fitting
data_to_fit = data_bay[['Beds', 'Baths', 'Home size', 'Lot size', 'Price']]

# get data summary
data_to_fit.describe()

# find and remove outliers
from scipy import stats
import numpy as np
z = np.abs(stats.zscore(data_to_fit[['Beds', 'Baths', 'Home size', 'Lot size', 'Price']]))
np.where(z > 3)
data_to_fit.iloc[1260]

data_no_outliers = data_to_fit[(z < 3).all(axis=1)]

# create pairplot
import seaborn as sns
sns.pairplot(data_no_outliers, x_vars = ['Beds', 'Baths', 'Home size', 'Lot size'], y_vars = 'Price')

# assign x and y variables
x = data_no_outliers[['Home size', 'Lot size', 'Beds', 'Baths']].values
y = data_no_outliers['Price'].values

# add column of ones to x
x = np.append(arr = np.ones((x.shape[0], 1)).astype(int), values = x, axis = 1)

# split data into test and training sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)

# fit data with multiple linear regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# predict test set
y_pred = regressor.predict(x_test)

# build model
import statsmodels.formula.api as sm
x_opt = x[:, [0, 1, 2, 3, 4]]
regressor_OLS = sm.OLS(endog = y, exog = x_opt).fit()
regressor_OLS.summary()




