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

cities_of_interest = ['San Francisco', 'San Jose', 'Oakland', 'Berkeley', 
                      'San Leandro', 'Hayward', 'Fremont', 'Richmond',
                      'Orinda', 'San Mateo', 'Redwood City', 'Palo Alto',
                      'Daly City', 'Woodside', 'Menlo Park', 'Los Gatos',
                      'Santa Clara', 'Cupertino', 'Los Altos', 'Sunnyvale',
                      'Mill Valley', 'Tiburon', 'Hillsborough', 'Piedmont']

data_of_interest = data_bay[data_bay['City'].isin(cities_of_interest)]

# Find the order
#my_order = cities_of_interest.groupby(by=["species"])["sepal_length"].median().iloc[::-1].index
city_order = data_of_interest.groupby('City').median().sort_values(by='Price',ascending=True).iloc[:,2].to_frame().reset_index()

# try seaborn
import seaborn as sns
fig, ax = plt.subplots(1, 1, figsize = (20,20))
ax = sns.boxplot(x = 'City', y = 'Price', data = data_of_interest,
                 showfliers = False, order = list(city_order['City']))
plt.xticks(rotation=45)
ax.set_ylim(0,8000000)

## major cities
#data_sanfrancisco = data_bay.loc[data_bay['City'] == 'San Francisco']
#data_sanjose = data_bay.loc[data_bay['City'] == 'San Jose']
#data_oakland = data_bay.loc[data_bay['City'] == 'Oakland']
#
## east bay
#data_berkeley = data_bay.loc[data_bay['City'] == 'Berkeley']
#data_sanleandro = data_bay.loc[data_bay['City'] == 'San Leandro']
#data_hayward = data_bay.loc[data_bay['City'] == 'Hayward']
#data_fremont = data_bay.loc[data_bay['City'] == 'Fremont']
#data_richmond = data_bay.loc[data_bay['City'] == 'Richmond']
#data_orinda = data_bay.loc[data_bay['City'] == 'Orinda']
#
## peninsula
#data_sanmateo = data_bay.loc[data_bay['City'] == 'San Mateo']
#data_redwoodcity = data_bay.loc[data_bay['City'] == 'Redwood City']
#data_paloalto = data_bay.loc[data_bay['City'] == 'Palo Alto']
#data_dalycity = data_bay.loc[data_bay['City'] == 'Daly City']
#data_woodside = data_bay.loc[data_bay['City'] == 'Woodside']
#data_menlopark = data_bay.loc[data_bay['City'] == 'Menlo Park']
#
## south bay
#data_losgatos = data_bay.loc[data_bay['City'] == 'Los Gatos']
#data_santaclara = data_bay.loc[data_bay['City'] == 'Santa Clara']
#data_cupertino = data_bay.loc[data_bay['City'] == 'Cupertino']
#data_losaltos = data_bay.loc[data_bay['City'] == 'Los Altos']
#data_sunnyvale = data_bay.loc[data_bay['City'] == 'Sunnvyale']
#
## north bay
#data_millvalley = data_bay.loc[data_bay['City'] == 'Mill Valley']
#data_tiburon = data_bay.loc[data_bay['City'] == 'Tiburon']





## calculate mean and stdev for each city, across all fields 
#city_means = data_bay.groupby('City').mean()
#city_stdevs = data_bay.groupby('City').agg(np.std, ddof=0)
#
## pull out price from mean and stdev dataframes 
#price_by_city_mean = city_means['Price']
#price_by_city_stdev = city_stdevs['Price']

# create boxplots
y = 1000000
fig, ax = plt.subplots()
bp1 = ax.boxplot(data_sanfrancisco['Price']/y, positions = [1], showfliers = False)
bp2 = ax.boxplot(data_sanjose['Price']/y, positions = [3], showfliers = False)

plt.xticks(list(range(1,23)), cities_of_interest)




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

