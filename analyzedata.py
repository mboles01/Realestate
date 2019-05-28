#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 10:03:23 2019

@author: michaelboles
"""

# set up working directory
import os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac

# import master dataset    
import pandas as pd
data_all = pd.read_csv('data_all.csv')

# import packages
import numpy as np
#import matplotlib.pyplot as plt

### PRICE ANALYSIS ###
prices_raw = data_all['Price']
prices = prices_raw/1000000

prices_mean = round(np.average(prices))
prices_median = np.median(prices)
prices_stdev = np.std(prices)

# set up histogram and text box
prices_binwidth = 0.1
prices_textbox = 'Average = $%.2f M \nMedian = $%.2f M \nStdev = $%.2f M' % (prices_mean, prices_median, prices_stdev)

# plot prices
from plotdata import plothist
plothist(prices, prices_binwidth, prices_textbox, 0, 5, 'Price ($M)', 'Counts')

prices_raw_SF = data_all.loc[data_all['City'] == 'San Francisco']




### PRICE / SQFT ANALYSIS ###
priceperft2_raw = data_all['Price']/data_all['Home size']
priceperft2 = priceperft2_raw[priceperft2_raw < 10000]

priceperft2_mean = round(np.average(priceperft2))
priceperft2_median = np.median(priceperft2)
priceperft2_stdev = np.std(priceperft2)

# set up histogram and text box
priceperft2_binwidth = 40
priceperft2_textbox = 'Average = $%.2f \nMedian = $%.2f \nStdev = $%.2f' % (priceperft2_mean, priceperft2_median, priceperft2_stdev)

# plot price per square foot
plothist(priceperft2, priceperft2_binwidth, priceperft2_textbox, 0, 2000, 'Price / sqft ($)', 'Counts')



