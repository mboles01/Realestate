#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 10:03:23 2019

@author: michaelboles
"""

# set up working directory
import os
#os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import master dataset    
import pandas as pd
data_all = pd.read_csv('data_all_2.csv')

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
from plotfunctions import plothist
plothist(prices, prices_binwidth, prices_textbox, 0, 5, 'Price ($M)', 'Counts')

prices_raw_SF = data_all.loc[data_all['City'] == 'San Francisco']




### PRICE / SQFT ANALYSIS ###

# home size
priceperftsqft_raw = data_all['Price']/data_all['Home size']
priceperftsqft = priceperftsqft_raw[priceperftsqft_raw < 10000]

priceperftsqft_mean = round(np.average(priceperftsqft))
priceperftsqft_median = np.median(priceperftsqft)
priceperftsqft_stdev = np.std(priceperftsqft)

# set up histogram and text box
priceperftsqft_binwidth = 40
priceperftsqft_textbox = 'Average = $%.2f \nMedian = $%.2f \nStdev = $%.2f' % (priceperftsqft_mean, priceperftsqft_median, priceperftsqft_stdev)

# plot price per square foot
plothist(priceperftsqft, priceperftsqft_binwidth, priceperftsqft_textbox, 0, 2000, 'Price / sqft ($)', 'Counts')


# lot size
lotpricepersqft_raw = data_all['Price']/(43560*data_all['Lot size'])

# apply corrections 
lotpricepersqft_temp = lotpricepersqft_raw[lotpricepersqft_raw < 100000]

# needs work: pull out spurious high-lot-price areas with acres & sqft switched
[row/43560 for row in lotpricepersqft_temp if row > 3000]
lotpricepersqft_temp[lotpricepersqft_temp > 3000]

lotpricepersqft_mean = round(np.average(lotpricepersqft))
lotpricepersqft_median = np.median(lotpricepersqft)
lotpricepersqft_stdev = np.std(lotpricepersqft)

# set up histogram and text box
lotpricepersqft_binwidth = 15
lotpricepersqft_textbox = 'Average = $%.2f \nMedian = $%.2f \nStdev = $%.2f' % (lotpricepersqft_mean, lotpricepersqft_median, lotpriceperftsqft_stdev)

# plot price per square foot
plothist(lotpriceperftsqft, lotpriceperftsqft_binwidth, lotpriceperftsqft_textbox, 0, 800, 'Price / lot sqft ($)', 'Counts')

