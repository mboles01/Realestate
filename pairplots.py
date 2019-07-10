# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:31:23 2019

@author: michaelboles
"""

# set up working directory
import os
#os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

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
data_to_fit.iloc[4422]

data_no_outliers = data_to_fit[(z < 3).all(axis=1)]

# create overall pairplot
import seaborn as sns
sns.pairplot(data_no_outliers, diag_kind='kde', kind = 'reg',
             plot_kws=dict(scatter_kws=dict(facecolor = 'b', edgecolor = 'w')))

# create pairplot with only price as y-axis
sns.set(style="ticks", color_codes=True)
sns.pairplot(data_no_outliers, 
             plot_kws=dict(scatter_kws=dict(facecolor = 'b', edgecolor = 'w')),
             x_vars = ['Beds', 'Baths', 'Home size', 'Lot size'], 
             y_vars = 'Price', kind = 'reg')


# not seeing strong correlations -- try same for only one zipcode
data_subset = data_clean.loc[data_clean['Zip'] == 95129]
data_subset_fit = data_subset[['Beds', 'Baths', 'Home size', 'Lot size', 'Price']]
sns.pairplot(data_subset, plot_kws=dict(scatter_kws=dict(facecolor = 'b', edgecolor = 'w')),
             x_vars = ['Beds', 'Baths', 'Home size', 'Lot size'], y_vars = 'Price', kind = 'reg')

# count number of unique zipcodes
data_bay['Zip'].nunique() 
# 214 zips - would be painful to manually enter drive/train times to SF, PA for each

# count frequency of each zipcode
data_bay['Zip'].value_counts()

### FITTING ###

# assign x and y variables
x = data_no_outliers[['Home size', 'Lot size', 'Beds', 'Baths']].values
y = data_no_outliers['Price'].values

# add column of ones to x
x = np.append(arr = np.ones((x.shape[0], 1)).astype(int), values = x, axis = 1)

## split data into test and training sets
#from sklearn.model_selection import train_test_split
#x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)
#
## fit data with multiple linear regression
#from sklearn.linear_model import LinearRegression
#regressor = LinearRegression()
#regressor.fit(x_train, y_train)
#
## predict test set
#y_pred = regressor.predict(x_test)

# build model from all data
import statsmodels.formula.api as smf
data_bay2 = data_bay.rename(index=str, columns={"Home size": "Homesize", "Lot size": "Lotsize"})
regressor_all = smf.ols(formula='Price ~ Homesize + Lotsize + Beds + Baths', data=data_bay2).fit()
regressor_all.summary()

# build model from data subset
import statsmodels.formula.api as smf
data_subset2 = data_subset.rename(index=str, columns={"Home size": "Homesize", "Lot size": "Lotsize"})
regressor_subset = smf.ols(formula='Price ~ Homesize + Lotsize + Beds + Baths', data=data_subset2).fit()
regressor_subset.summary()



