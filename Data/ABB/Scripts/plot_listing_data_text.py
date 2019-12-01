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

# replace punctuation with spaces
import string
listings_text2 = listings_text1.replace('['+string.punctuation+']', ' ', regex=True)

## replace double or triple spaces with single
#listings_text3 = listings_text2.replace('  ', ' ').replace('   ', ' ')

# make all lowercase
listings_text3 = listings_text2.apply(lambda x: x.astype(str).str.lower())

# split and lemmatize text
import nltk
w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()

def lemmatize_text(text):
    return [lemmatizer.lemmatize(w) for w in w_tokenizer.tokenize(text)]

summaries_lemmatized = listings_text3['summary'].apply(lemmatize_text)

# count words

# create word frequency dictionary across all listings and sort
df_word_count = pd.DataFrame(data = [], columns = ['Word', 'Count']).set_index('Word')
for row in summaries_lemmatized[0:9]:
    for word in row:
        df_word_count_temp = pd.DataFrame(data = [[word, 1]], 
                                          columns = ['Word', 'Count']).set_index('Word')
        
        df_word_count = df_word_count_temp.merge(df_word_count, 
                                on='Word', how='outer')
        
df_word_count = df_word_count.sum(axis=1)
df_word_count.rename('Count') # does it work? not sure
df_word_count.name

# remove generic words
words_to_remove = ['is', 'a', 'the', 'and', 'our', 'are', 'this', 
                   'with', 'and', 'you', 'your', 'to', 'of', 'in']









# filter, token, lemmatize text
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
cv_fit = cv.fit_transform(summaries_list)
feature_names = cv.get_feature_names()
feature_vectors = cv_fit.toarray()
















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


