#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:25:15 2019

@author: michaelboles
"""

# set up working directory
import os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate/Data/ABB/Data/San Francisco') # Mac
#os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import packages
import pandas as pd
import numpy as np

# import full dataset 
data_all_raw = pd.read_csv('./listings 2.csv')

# get column names 
data_colnames = list(data_all_raw)


# get columns of interest: 
    
data_all = data_all_raw[['id', 'name', 'host_name',
                         'neighbourhood', 'latitude', 'longitude',
                         'bedrooms', 'bathrooms', 'square_feet', 
                         'property_type', 'room_type',
                         'guests_included', 'extra_people', 'minimum_nights',
                         'availability_30', 'availability_90',
                         'number_of_reviews', 'review_scores_rating', 'last_review',
                         'price', 'cleaning_fee', 'security_deposit']].copy()

# CLEAN DATA

# convert prices from string '$__' to float
data_all[['extra_people','price','cleaning_fee','security_deposit']] = data_all[['extra_people','price','cleaning_fee','security_deposit']].replace('[\$,]', '', regex=True).astype(float)

# remove outliers: > 5 beds, > 4 baths, > $1000/night
data_1 = data_all[(data_all['bedrooms'] < 5) & (data_all['bathrooms'] < 4) & (data_all['bathrooms'] < 4) & (data_all['price'] < 1000)]



# visualize key metrics
import matplotlib as plt
import seaborn as sns

def corrfunc(x, y, **kws):
    r = x.corr(y)
    ax = plt.gca()
    ax.annotate(r'$R^{2}$ = ' + str(round(r, 2)), xy=(.1, .9), xycoords=ax.transAxes, backgroundcolor = 'white')

g = sns.pairplot(data_1, diag_kind = 'kde', kind = 'reg',
             plot_kws=dict(line_kws=dict(color = '#3148a3'), 
                           scatter_kws=dict(facecolor = '#5797ff', edgecolor = '#3148a3', 
                                            linewidth = 0.33, alpha = 0.1, s = 20)),
             x_vars = ['bedrooms', 'bathrooms', 'price'], 
             y_vars = ['bedrooms', 'bathrooms', 'price'])
g.map_lower(corrfunc)








