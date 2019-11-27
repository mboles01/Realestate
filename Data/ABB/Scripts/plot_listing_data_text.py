#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 16:43:36 2019

@author: michaelboles
"""

# set up working directory
import os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate/Data/ABB') # Mac

# import standard packages
import numpy as np
import pandas as pd

# import custom histogram plotter
import sys
sys.path.append('./Scripts')
from plotfunctions import plothist, texthist, plothist_categorical

# import cleaned SF listing dataset with text descriptions - doesn't work - can't save csv
listings_sf_clean = pd.read_csv('./Data/Clean/San_Francisco/listings_sf_data_clean_full.csv')

listings_sf_clean_text = listings_sf_clean[['id', 'name', 'host_name',
                                    'name', 'summary', 'space', 'description',
                                    'neighborhood_overview', 'notes', 'transit', 
                                    'access', 'interaction', 'house_rules']]

# replace NaNs with empty string
listings_text1 = listings_sf_clean_text.replace(np.nan, '', regex=True)

# replace hyphens with spaces
summaries_1 = listings_text1.replace('-' ,'', regex=True)

# create list of summaries
summaries_2 = list(summaries_1['summary'])

# strip punctuation
import string
summaries_3 = [line.translate(str.maketrans('', '', string.punctuation)) for line in summaries_2]

# make all lowercase
[line.lower() for line in summaries_3]

# split into words
summaries_split = [line.split() for line in summaries_list]

[line.translate(None, line.punctuation) for line in summaries_split]

[print(line) for line in summaries_split]

# count frequency of words
from collections import Counter
counts = Counter(summaries_list)

# filter, token, lemmatize text
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
cv_fit = cv.fit_transform(summaries_list)
feature_names = cv.get_feature_names()
feature_vectors = cv_fit.toarray()

# functioning example
texts=["dog cat fish","dog cat cat","fish bird", 'bird']
cv = CountVectorizer()
cv_fit=cv.fit_transform(texts)
cv.get_feature_names()
cv_fit.toarray()















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


