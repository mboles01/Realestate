#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 19:01:52 2019

@author: michaelboles
"""

# set up working directory
import os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate/Data/ABB') # Mac

# import standard packages
import pandas as pd
import seaborn as sns

# import cleaned SF listing dataset
listings_sf_clean = pd.read_csv('./Data/Clean/San_Francisco/listings_sf_data_clean.csv')

# visualize key metrics
import matplotlib.pyplot as plt

def corrfunc(x, y, **kws):
    r = x.corr(y)
    ax = plt.gca()
    ax.annotate(r'$R^{2}$ = ' + str(round(r, 2)), xy=(.1, .9), xycoords=ax.transAxes, backgroundcolor = 'white')

g = sns.pairplot(listings_sf_clean, diag_kind = 'kde', kind = 'reg',
             plot_kws=dict(line_kws=dict(color = '#3148a3'), 
                           scatter_kws=dict(facecolor = '#5797ff', edgecolor = '#3148a3', 
                                            linewidth = 0.33, alpha = 0.1, s = 20)),
             x_vars = ['bedrooms', 'bathrooms', 'price', 'number_of_reviews', 'reviews_per_month', 'monthly_revenue'], 
             y_vars = ['bedrooms', 'bathrooms', 'price', 'number_of_reviews', 'reviews_per_month', 'monthly_revenue'])

#g.map_upper(sns.regplot, truncate=True)
g.map_lower(corrfunc)

x_vars = ['bedrooms', 'bathrooms', 'price', 'number_of_reviews', 'reviews_per_month', 'monthly_revenue']
y_vars = ['bedrooms', 'bathrooms', 'price', 'number_of_reviews', 'reviews_per_month', 'monthly_revenue']


#for i in range(len(x_vars)):
#    for j in range(len(y_vars)):
#        
#        g.axes[i,j].set_xlim((0,np.max(listings_5[x_vars[i])))
#        g.axes[i,j].set_ylim((0,np.max(listings_5[y_vars[j])))
#        

g.savefig('.\Images\pairplot_5.jpg', dpi=300)


# plot histograms of features
plt.rcParams["patch.force_edgecolor"] = True
ax1, ax2, ax3, ax4, ax5 = plt.subplots(1,5, figsize = (20,4))
ax1 = sns.distplot(listings_sf_clean['monthly_revenue'], kde=False); plt.xlim(0,20000)
ax2 = sns.distplot(listings_sf_clean['price'], kde=False); plt.xlim(0,1000)
ax3 = sns.distplot(listings_sf_clean['bedrooms'], kde=False); plt.xlim(0,5)
ax4 = sns.distplot(listings_sf_clean['number_of_reviews'], kde=False); plt.xlim(0,500)
ax5 = sns.distplot(listings_sf_clean['reviews_per_month'], kde=False); plt.xlim(0,10)

# plot kde (kernel density estimate) plots of features
g = sns.kdeplot(listings_sf_clean['monthly_revenue'], shade=True, clip=(0,20000))
g = sns.kdeplot(listings_sf_clean['price'], shade=True, clip=(0,1000))
g = sns.kdeplot(listings_sf_clean['bedrooms'], shade=True, clip=(0,10))
