# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:31:23 2019

@author: michaelboles
"""

# set up working directory
import os
#os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import packages
import pandas as pd
from scipy import stats
import numpy as np
import statsmodels.formula.api as smf
import seaborn as sns

# import master dataset    
data_bay_withtimes = pd.read_csv('./data/data_bay_withtimes.csv')

# add shorter commute time column
data_bay_withtimes['Min commute'] = data_bay_withtimes[['SF time', 'PA time']].min(axis=1)

# remove spaces in column names - necessary for OLS?
data_bay_withtimes.columns = data_bay_withtimes.columns.str.replace(' ', '_')

# format/clean -- remove spaces, drop rows with zeros, NaNs
data_to_fit = data_bay_withtimes[['Zip', 'Beds', 'Baths', 'Home_size', 'Lot_size', 'SF_time', 'PA_time', 'Min_commute', 'Price']]
data_temp1 = data_to_fit.dropna()
data_temp2 = data_temp1[(data_temp1 != 0).all(1)]
data_temp3 = data_temp2[data_temp2['Lot_size'] < 100000]

# create overall pairplot
sns.pairplot(data_temp3, diag_kind = 'kde', kind = 'reg',
             plot_kws = dict(scatter_kws = dict(edgecolor = 'w')))

# count number, frequency of unique zipcodes
numzips = data_bay_withtimes['Zip'].nunique()
topzips = data_bay_withtimes['Zip'].value_counts()

# option to select subset of zipcodes
lozip = 95029; hizip = 95031
data_temp4 = data_temp3[(data_temp3['Zip'] > lozip) & (data_temp3['Zip'] < hizip)]
#data_temp4 = data_temp3

# option to remove outliers
z = np.abs(stats.zscore(data_temp4[['Beds', 'Baths', 'Home_size', 'Lot_size', 
                                  'SF_time', 'PA_time', 'Min_commute', 'Price']]))
data_to_fit = data_temp4[(z < 3).all(axis=1)]
#data_to_fit = data_temp4

# create subset pairplot
sns.pairplot(data_to_fit.drop('Zip', axis = 1), diag_kind = 'kde', kind = 'reg',
             plot_kws = dict(scatter_kws = dict(edgecolor = 'w')))

# create pairplot with only price as y-axis
sns.set(style="ticks", color_codes=True)
sns.pairplot(data_to_fit, 
             plot_kws=dict(scatter_kws=dict(edgecolor = 'w')),
             x_vars = ['Beds', 'Baths', 'Home_size', 'Lot_size', 
                       'SF_time', 'PA_time', 'Min_commute'], 
             y_vars = 'Price', kind = 'reg')


# query count, mean, stdev etc. of selected data
data_to_fit.describe()


### BUILD MODEL ###



# build model from data
formula = 'Price ~ Home_size + Lot_size + Beds + Baths + Min_commute + SF_time + PA_time'
regressor = smf.ols(formula, data = data_temp3).fit()








# count number, frequency of unique zipcodes
data_bay['Zip'].nunique() 
data_bay['Zip'].value_counts()

# remove zeros, NaNs, index column
data_temp2 = data_all.dropna()
data_clean = data_temp2[(data_temp2 != 0).all(1)]


# select only columns for fitting
data_to_fit = data_bay[['Beds', 'Baths', 'Home size', 'Lot size', 'Price']]

# get data summary
data_to_fit.describe()

# find and remove outliers
z = np.abs(stats.zscore(data_to_fit[['Beds', 'Baths', 'Home size', 'Lot size', 'Price']]))
np.where(z > 3)
data_to_fit.iloc[4422]

data_no_outliers = data_to_fit[(z < 3).all(axis=1)]

# try same for only one zipcode
data_subset = data_clean.loc[data_clean['Zip'] == 95129]
data_subset_fit = data_subset[['Beds', 'Baths', 'Home size', 'Lot size', 'Price']]


### FITTING ###

# assign x and y variables
x = data_no_outliers[['Home size', 'Lot size', 'Beds', 'Baths']].values
y = data_no_outliers['Price'].values

# add column of ones to x
x = np.append(arr = np.ones((x.shape[0], 1)).astype(int), values = x, axis = 1)


### insert additional features ###
data_bay_withtimes = pd.read_csv('./data/data_bay_withtimes.csv')
data_bay_withtimes.columns = data_bay_withtimes.columns.str.replace(' ', '_')
data_temp1 = data_bay_withtimes.dropna()
data_temp2 = data_temp1
#data_temp2 = data_temp1[data_temp1['Zip'].isin([94618])]
data_temp3 = data_temp2[(data_temp2 != 0).all(1)]
data_temp3['Min_commute'] = data_temp3[['SF_time','PA_time']].min(axis=1)

z = np.abs(stats.zscore(data_temp3[['Beds', 'Baths', 'Home_size', 'Lot_size', 
                                  'Price', 'SF_time', 'PA_time', 'Min_commute']]))
data_to_fit = data_temp3[(z < 3).all(axis=1)]
data_to_fit.describe()
data_temp3.describe()

# build model from data
import statsmodels.formula.api as smf

formula = ='Price ~ Home_size + Lot_size + Beds + Baths + Min_commute + SF_time + PA_time'
regressor = smf.ols(formula, data = data_temp3).fit()



regressor.summary()




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



