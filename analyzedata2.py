#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 10:03:23 2019

@author: michaelboles
"""

# set up working directory
import os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
#os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import master dataset    
data_bay = pd.read_csv('./data/data_bay.csv')

# count number of entries for each city/town
city_counts = data_bay.groupby('City').count().iloc[:,1].to_frame()
city_counts.columns = ['Count']

# display cities with most listings first
city_counts_sorted = city_counts.sort_values('Count', ascending = False)

# select cities of interest
city_info = pd.DataFrame({'City': [], 'Count': [], 'Average Price': [], 'Stdev': []})

cities_of_interest = ['San Francisco', 'San Jose', 'Oakland', 'Berkeley', 'San Leandro',
                      'Hayward', 'Fremont', 'Richmond', 'Vallejo', 'Antioch', 'Walnut Creek',
                      'Orinda', 'San Mateo', 'Redwood City', 'Palo Alto', 'Mountain View',
                      'Daly City', 'Woodside', 'Menlo Park',
                      'Santa Clara', 'Cupertino', 'Los Altos', 'Los Gatos', 'Sunnyvale',
                      'Mill Valley', 'Tiburon', 'Sausalito', 'Hillsborough', 'Piedmont']


# create dataframe with only cities of interest
data_of_interest = data_bay[data_bay['City'].isin(cities_of_interest)]

# add a column for price per lot sqft
data_of_interest.insert(loc = 6, column = 'Price per lot sqft', value = data_of_interest['Price']/data_of_interest['Lot size'])

# Determine order
city_order_price = data_of_interest.groupby('City').median().sort_values(by='Price',ascending=True).iloc[:,2].to_frame().reset_index()
city_order_pricesqft = data_of_interest.groupby('City').median().sort_values(by='Price per lot sqft',ascending=True).iloc[:,3].to_frame().reset_index()


# create seaborn box + strip plot
import seaborn as sns
import matplotlib.ticker as ticker

fig, ax = plt.subplots(1, 1, figsize = (60,30))

ax = sns.boxplot(x = 'City', y = 'Price', data = data_of_interest, 
                 showfliers = False, order = list(city_order_price['City']), linewidth = 5)
ax = sns.stripplot(x = 'City', y = 'Price', data = data_of_interest,
                 order = list(city_order_price['City']), jitter = 0.25, size = 15,
                 linewidth = 3, edgecolor = 'black', alpha = 0.5)

# set axis properties
plt.xticks(rotation=45, fontname = 'Helvetica', fontsize = 42, ha = 'right')
plt.yticks(fontname = 'Helvetica', fontsize = 42)


plt.xlabel('City or Town', fontsize = 55, fontname = 'Arial', fontweight = 'bold')
plt.ylabel('Single Family Home Price ($M)', fontsize = 55, fontname = 'Arial', 
           fontweight = 'bold')

scale = 1000000; ax.set_ylim(0, 8000000); ax.yaxis.labelpad = 25
ticks = ticker.FuncFormatter(lambda y, pos: '{0:g}'.format(y/scale))
ax.xaxis.set_tick_params(width = 3, length = 15)
ax.yaxis.set_tick_params(width = 3, length = 15)
ax.yaxis.set_major_formatter(ticks)
plt.setp(ax.spines.values(), linewidth = 3)


# do the same for price per lot sqft
fig, ax = plt.subplots(1, 1, figsize = (60,30))

ax = sns.boxplot(x = 'City', y = 'Price per lot sqft', data = data_of_interest, 
                 showfliers = False, order = list(city_order_pricesqft['City']), linewidth = 5)
ax = sns.stripplot(x = 'City', y = 'Price per lot sqft', data = data_of_interest,
                 order = list(city_order_pricesqft['City']), jitter = 0.25, size = 15,
                 linewidth = 3, edgecolor = 'black', alpha = 0.5)

# set axis properties
plt.xticks(rotation=45, fontname = 'Helvetica', fontsize = 42, ha = 'right')
plt.yticks(fontname = 'Helvetica', fontsize = 42)


plt.xlabel('City or Town', fontsize = 55, fontname = 'Arial', fontweight = 'bold')
plt.ylabel('Lot price per sqft ($)', fontsize = 55, fontname = 'Arial', 
           fontweight = 'bold')

ax.set_ylim(0, 2000); ax.yaxis.labelpad = 25
ticks = ticker.FuncFormatter(lambda y, pos: '{0:g}'.format(y))
ax.xaxis.set_tick_params(width = 3, length = 15)
ax.yaxis.set_tick_params(width = 3, length = 15)
ax.yaxis.set_major_formatter(ticks)
plt.setp(ax.spines.values(), linewidth = 3)





# other seaborn plot options
#
## boxenplot
#fig, ax = plt.subplots(1, 1, figsize = (20,10))
#ax = sns.boxenplot(x = 'City', y = 'Price', data = data_of_interest,
#                 outlier_prop = 0.01, order = list(city_order['City']))
#plt.xticks(rotation=45)
#plt.xlabel('City or Town', fontsize = 18, fontname = 'Arial', fontweight = 'bold')
#plt.ylabel('Single Family Home Price ($M)', fontsize = 18, fontweight = 'bold')
#ax.set_ylim(0,8000000)
#ticks = ticker.FuncFormatter(lambda y, pos: '{0:g}'.format(y/scale))
#ax.yaxis.set_major_formatter(ticks)
#
## violinplot
#fig, ax = plt.subplots(1, 1, figsize = (20,10))
#ax = sns.violinplot(x = 'City', y = 'Price', data = data_of_interest,
#                 outlier_prop = 0.01, order = list(city_order['City']))
#plt.xticks(rotation=45)
#plt.xlabel('City or Town', fontsize = 18, fontname = 'Arial', fontweight = 'bold')
#plt.ylabel('Single Family Home Price ($M)', fontsize = 18, fontweight = 'bold')
#ax.set_ylim(0,8000000)
#ticks = ticker.FuncFormatter(lambda y, pos: '{0:g}'.format(y/scale))
#ax.yaxis.set_major_formatter(ticks)
#
## stripplot
#fig, ax = plt.subplots(1, 1, figsize = (20,10))
#ax = sns.stripplot(x = 'City', y = 'Price', data = data_of_interest,
#                 order = list(city_order['City']))
#plt.xticks(rotation=45)
#plt.xlabel('City or Town', fontsize = 18, fontname = 'Arial', fontweight = 'bold')
#plt.ylabel('Single Family Home Price ($M)', fontsize = 18, fontweight = 'bold')
#ax.set_ylim(0,8000000)
#ticks = ticker.FuncFormatter(lambda y, pos: '{0:g}'.format(y/scale))
#ax.yaxis.set_major_formatter(ticks)
#
## swarmplot
#fig, ax = plt.subplots(1, 1, figsize = (20,10))
#ax = sns.swarmplot(x = 'City', y = 'Price', data = data_of_interest,
#                 order = list(city_order['City']))
#plt.xticks(rotation=45)
#plt.xlabel('City or Town', fontsize = 18, fontname = 'Arial', fontweight = 'bold')
#plt.ylabel('Single Family Home Price ($M)', fontsize = 18, fontweight = 'bold')
#ax.set_ylim(0,8000000)
#ticks = ticker.FuncFormatter(lambda y, pos: '{0:g}'.format(y/scale))
#ax.yaxis.set_major_formatter(ticks)








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

