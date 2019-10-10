# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:14:46 2019

@author: BolesMi
"""

# set up working directory
import os
#os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import packages
import pandas as pd
import matplotlib.pyplot as plt

# import all listing data
data_all = pd.read_csv('./Data/listings/data_all_raw.csv', index_col = 0)

# import dataset with price residuals (actual - predicted price)
data_residuals = pd.read_csv('./Data/listings/data_all_price_predictions.csv')

# import sf neighborhoods by zipcode 
sf_neighborhoods = pd.read_csv('./Data/data by zipcode/sf_neighborhoods.csv').iloc[:,0:2]

# pull out only sf listings from both
sf_data_all = data_all[data_all['City'] == 'San Francisco']
sf_data_residuals = data_residuals[data_residuals['City'] == 'San Francisco']

# merge sf listings with neighborhood data
sf_data_all_neighborhoods = sf_neighborhoods.merge(sf_data_all, on='Zip', how='right')
sf_data_residuals_neighborhoods = sf_neighborhoods.merge(sf_data_residuals, on='Zip', how='right')

# option to remove a neighborhood
sf_data_all_neighborhoods = sf_data_all_neighborhoods[sf_data_all_neighborhoods.Neighborhood != 'Chinatown']
sf_data_residuals_neighborhoods = sf_data_residuals_neighborhoods[sf_data_residuals_neighborhoods.Neighborhood != 'South of Market']

# Determine order
neighborhood_order_price = sf_data_all_neighborhoods.groupby('Neighborhood').median().sort_values(by = 'Price', ascending = True).iloc[:,-1].to_frame().reset_index()
neighborhood_order_residuals = sf_data_residuals_neighborhoods.groupby('Neighborhood').median().sort_values(by = 'Price difference', ascending = True).iloc[:,-1].to_frame().reset_index()

# prices: create seaborn box + strip plot
import seaborn as sns
import matplotlib.ticker as ticker

fig, ax = plt.subplots(1, 1, figsize = (60,30))

ax = sns.boxplot(x = 'Neighborhood', y = 'Price', data = sf_data_all_neighborhoods, 
                 showfliers = False, order = list(neighborhood_order_price['Neighborhood']), linewidth = 5)
ax = sns.stripplot(x = 'Neighborhood', y = 'Price', data = sf_data_all_neighborhoods,
                 order = list(neighborhood_order_price['Neighborhood']), jitter = 0.25, size = 15,
                 linewidth = 3, edgecolor = 'black', alpha = 0.5)

# set axis properties
plt.xticks(rotation=45, fontname = 'Helvetica', fontsize = 42, ha = 'right')
plt.yticks(fontname = 'Helvetica', fontsize = 42)


plt.xlabel('Neighborhood', fontsize = 55, fontname = 'Arial', fontweight = 'bold')
plt.ylabel('Price ($M)', fontsize = 55, fontname = 'Arial', 
           fontweight = 'bold')

scale = 1000000; ax.set_ylim(0, 10000000); ax.yaxis.labelpad = 25
ticks = ticker.FuncFormatter(lambda y, pos: '{0:g}'.format(y/scale))
ax.xaxis.set_tick_params(width = 3, length = 15)
ax.yaxis.set_tick_params(width = 3, length = 15)
ax.yaxis.set_major_formatter(ticks)
plt.setp(ax.spines.values(), linewidth = 3)



# residuals: create seaborn box + strip plot

fig, ax = plt.subplots(1, 1, figsize = (60,30))

plt.axhline(y = 0, color = 'k', linestyle = ':', linewidth = 2)

ax = sns.boxplot(x = 'Neighborhood', y = 'Price difference', data = sf_data_residuals_neighborhoods, 
                 showfliers = False, order = list(neighborhood_order_residuals['Neighborhood']), linewidth = 5)
ax = sns.stripplot(x = 'Neighborhood', y = 'Price difference', data = sf_data_residuals_neighborhoods,
                 order = list(neighborhood_order_residuals['Neighborhood']), jitter = 0.25, size = 15,
                 linewidth = 3, edgecolor = 'black', alpha = 0.5)

# set axis properties
plt.xticks(rotation=45, fontname = 'Helvetica', fontsize = 42, ha = 'right')
plt.yticks(fontname = 'Helvetica', fontsize = 42)


plt.xlabel('Neighborhood', fontsize = 55, fontname = 'Arial', fontweight = 'bold')
plt.ylabel('Actual - predicted price ($M)', fontsize = 55, fontname = 'Arial', 
           fontweight = 'bold')

scale = 1000000; ax.set_ylim(-1000000, 3000000); ax.yaxis.labelpad = 25
ticks = ticker.FuncFormatter(lambda y, pos: '{0:g}'.format(y/scale))
ax.xaxis.set_tick_params(width = 3, length = 15)
ax.yaxis.set_tick_params(width = 3, length = 15)
ax.yaxis.set_major_formatter(ticks)
plt.setp(ax.spines.values(), linewidth = 3)
