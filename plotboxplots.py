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
import matplotlib.pyplot as plt

# import master dataset    
data_bay = pd.read_csv('./Data/listings/data_bay.csv')

# also import dataset with price residuals (actual - predicted)
data_residuals = pd.read_csv('./Data/listings/data_all_price_predictions.csv')

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


cities_of_interest2 = ['San Francisco', 'San Jose', 'Oakland', 'Berkeley', 'San Leandro',
                      'Hayward', 'Fremont', 'Richmond', 'Vallejo', 'Antioch', 'Walnut Creek',
                      'Orinda', 'San Mateo', 'Redwood City', 'Palo Alto', 'Mountain View',
                      'Daly City', 'Menlo Park', 'East Palo Alto', 'San Anselmo',
                      'Santa Clara', 'Cupertino', 'Los Altos', 'Los Gatos', 'Sunnyvale',
                      'Mill Valley', 'Tiburon', 'Sausalito', 'Alameda', 'Piedmont']



# create dataframe with only cities of interest
data_of_interest = data_bay[data_bay['City'].isin(cities_of_interest)]
data_of_interest_residuals = data_residuals[data_residuals['City'].isin(cities_of_interest2)]

# add a column for price per lot sqft
data_of_interest.insert(loc = 6, column = 'Price per lot sqft', value = data_of_interest['Price']/data_of_interest['Lot size'])

# Determine order
city_order_price = data_of_interest.groupby('City').median().sort_values(by='Price',ascending=True).iloc[:,2].to_frame().reset_index()
city_order_pricesqft = data_of_interest.groupby('City').median().sort_values(by='Price per lot sqft',ascending=True).iloc[:,3].to_frame().reset_index()
city_order_residuals = data_of_interest_residuals.groupby('City').median().sort_values(by = 'Price difference', ascending = True).iloc[:,-1].to_frame().reset_index()

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


plt.xlabel('Location', fontsize = 55, fontname = 'Arial', fontweight = 'bold')
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


plt.xlabel('Location', fontsize = 55, fontname = 'Arial', fontweight = 'bold')
plt.ylabel('Land Price Per Square Foot ($)', fontsize = 55, fontname = 'Arial', 
           fontweight = 'bold')

ax.set_ylim(0, 2000); ax.yaxis.labelpad = 25
ticks = ticker.FuncFormatter(lambda y, pos: '{0:g}'.format(y))
ax.xaxis.set_tick_params(width = 3, length = 15)
ax.yaxis.set_tick_params(width = 3, length = 15)
ax.yaxis.set_major_formatter(ticks)
plt.setp(ax.spines.values(), linewidth = 3)


# and do the same for price difference
fig, ax = plt.subplots(1, 1, figsize = (60,30))

plt.axhline(y = 0, color = 'k', linestyle = ':', linewidth = 2)

ax = sns.boxplot(x = 'City', y = 'Price difference', data = data_of_interest_residuals, 
                 showfliers = False, order = list(city_order_residuals['City']), linewidth = 5)
ax = sns.stripplot(x = 'City', y = 'Price difference', data = data_of_interest_residuals,
                 order = list(city_order_residuals['City']), jitter = 0.25, size = 15,
                 linewidth = 3, edgecolor = 'black', alpha = 0.5)

# set axis properties
plt.xticks(rotation = 45, fontname = 'Helvetica', fontsize = 42, ha = 'right')
plt.yticks(fontname = 'Helvetica', fontsize = 42)


plt.xlabel('Location', fontsize = 55, fontname = 'Arial', fontweight = 'bold')
plt.ylabel('Actual - predicted price ($M)', fontsize = 55, fontname = 'Arial', 
           fontweight = 'bold')

scale = 1000000; ax.set_ylim(-1200000, 2500000); ax.yaxis.labelpad = 25
ticks = ticker.FuncFormatter(lambda y, pos: '{0:g}'.format(y/scale))
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