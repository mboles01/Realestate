#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 16:43:36 2019

@author: michaelboles
"""

# set up working directory
import os
#os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate/Data/ABB') # Mac
os.chdir('/Users/bolesmi/Lam/Coding/Python/2019/Realestate/Data/ABB') # PC

# import standard packages
import numpy as np
import pandas as pd

# import cleaned SF listing dataset with text descriptions
listings_bow = pd.read_csv('./Data/Clean/San_Francisco/listings_sf_data_bow.csv', 
                           compression='gzip')

# separate into high- and low-revenue categories
listings_highlow = listings_bow[listings_bow['revenue_category'] != 'Medium']

## check first and last bow entries of a single listing
#listings_highlow.iloc[0]


### ANALYSIS ###

# stipulate x- and y-variables
X = listings_highlow.iloc[:,4:]
y = listings_highlow['revenue_category']

### PCA - component axes that maximize explained variance - unsupervised, no consideration of dependent variable ###

# apply principal component analysis (PCA)
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
X = pca.fit_transform(X)
explained_variance = pca.explained_variance_ratio_

### LDA - component axes that maximize class separation - supervised, considers dependent variable ### 







### PLOTTING ###

# visualize PCA result
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
x_set, y_set = X, y
x1, x2 = np.meshgrid(np.arange(start = x_set[:, 0].min() - 1, 
                               stop = x_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = x_set[:, 1].min() - 1, 
                               stop = x_set[:, 1].max() + 1, step = 0.01))
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
                c = ListedColormap(('blue', 'red'))(i), label = j,
                s = .5)
plt.title('PCA: high- vs. low-revenue Airbnbs using listing text BoWs')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.legend(markerscale = 10)
plt.savefig('./Images/NLP/PCA_Airbnb_text.jpg', bbox_inches='tight', dpi = 600) 
plt.show()









### COMBINED WORD ANALYSIS ACROSS LISTINGS ###

# create word frequency dictionary across all listings
from nlp_functions import count_words
listings_wordcount = count_words(listings_text9)

# sort word frequency dictionary
import operator
listings_wordcount_sorted = sorted(listings_wordcount.items(),key=operator.itemgetter(1),reverse=True)
df_listings_wordcount_sorted = pd.DataFrame(data = listings_wordcount_sorted, columns =['Word', 'Count'])























### PLOT HISTOGRAMS - NUMERICAL ###

# revenue estimates

histogram_text = texthist(data = listings_sf_clean['monthly_revenue'], 
                          divide_median=1, divide_stdev=1, rounding=0,
                          decimals = 0, units = '', dollars = True)

name = './Images/monthly_revenue.jpg'
plothist(data = listings_sf_clean['monthly_revenue'], nbins = 35, nxticks = 6, roundx = 3, 
         textbox = histogram_text, text_xpos = .94, xmin = 0, xmax = 20000, shift = None,
         xlabel = 'Revenue per month ($)', ylabel = 'Counts', figure_name = name)



### PLOT HISTOGRAMS - CATEGORICAL ###

# property type

name = './Images/property_type.jpg'

plothist_categorical(data = listings_sf_clean['property_type'], ncategories = 7, 
                     title = 'Property type', rotation = 45, figure_name = name,
                     xdim = 7, ydim = 7)


