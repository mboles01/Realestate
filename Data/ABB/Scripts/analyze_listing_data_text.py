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
                                    'summary', 'space', 'description',
                                    'neighborhood_overview', 'notes', 'transit', 
                                    'access', 'interaction', 'house_rules', 
                                    'monthly_revenue', 'revenue_category']]

# replace NaNs with empty string
listings_text1 = listings_sf_clean_text.replace(np.nan, '', regex=True)

# replace punctuation with spaces
import string
listings_text2 = listings_text1.replace('['+string.punctuation+']', ' ', regex=True)

# make all lowercase
listings_text3 = listings_text2.apply(lambda x: x.astype(str).str.lower())

# combine text of single listing
listings_text4 = listings_text3.copy()

listings_text4['Combined text'] = listings_text4[['name', 'summary', 'space', 'description', 
              'neighborhood_overview', 'notes', 'transit', 'access', 'interaction', 
              'house_rules']].apply(lambda x: ''.join(x), axis=1)



# create bag of words vector for listing text

# tokenize text
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
corpus = listings_text4['Combined text']
bagofwords = vectorizer.fit_transform(corpus).toarray()

# recombine numerical listing data with bag of words vector









### COMBINED WORD ANALYSIS ACROSS LISTINGS ###

# split and lemmatize text for columns of interest: name, summary, space, description
from nlp_functions import lemmatize_text
listings_text5 = listings_text4['Combined text'].apply(lemmatize_text)

# create word frequency dictionary across all listings
from nlp_functions import count_words
listings_wordcount = count_words(listings_text5)

# sort word frequency dictionary
import operator
listings_wordcount_sorted = sorted(listings_wordcount.items(),key=operator.itemgetter(1),reverse=True)
df_listings_wordcount_sorted = pd.DataFrame(data = listings_wordcount_sorted, columns =['Word', 'Count'])

# remove generic words
summaries_topcount = df_listings_wordcount_sorted[0:50]
summaries_words_to_remove = ['the', 'and', 'a', 'to', 'is', 'in', 'of', 'with', 
                             'for', 'room', 'are', 'from', 'this', 'you', 'on', 
                             'our', 'or', 'it', 'have', 'guest', 'be', 'are', 
                             '1', '2', 's', 'one', 'ha']

df_summaries_filtered = df_listings_wordcount_sorted[~df_listings_wordcount_sorted['Word'].isin(summaries_words_to_remove)]






















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


