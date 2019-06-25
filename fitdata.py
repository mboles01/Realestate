# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:31:23 2019

@author: BolesMi
"""

# set up working directory
import os
#os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import master dataset    
import pandas as pd
data_all = pd.read_csv('data_clean.csv')

# assign x and y variables
x = data_all[['Home size', 'Lot size', 'Beds', 'Baths']].values
y = data_all['Price'].values

# split data into test and training sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)

from sklearn.linear_model import LinearRegression
