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

# create word frequency dictionary across all listings and sort - doesn't work yet
words = []
wordfreq = []
df_word_count = pd.DataFrame(data = [], columns = ['Word', 'Count']).set_index('Word')
for row in summaries_lemmatized[0:10]:
#    print(row)
#    print('//////')
    for word in row:
#        print(word)
#        print('/')
        df_word_count_temp = pd.DataFrame(data = [[word, 1]], 
                                          columns = ['Word', 'Count']).set_index('Word')
        df_word_count_sum = df_word_count_temp.merge(df_word_count_sum, 
                                on='Word', how='outer').sum(axis=1)

        
        words.append(word)
        wordfreq.append(row.count(word))

    
word_count = dict(list(zip(summaries_lemmatized, wordfreq)))
word_count_sorted = sorted(word_count.items(), key=lambda kv: kv[1], reverse=True)
df_word_count_all = pd.DataFrame(word_count_sorted).merge(df_word_count, 
                                on='Zip', how='outer').sum(axis=1)


df_word_count = pd.DataFrame(word_count_sorted)

# create word frequency dictionary across two listings, sort and merge
wordfreq1 = []
for word in summaries_lemmatized[1]:
    wordfreq1.append(summaries_lemmatized[1].count(word))

word_count_1 = dict(list(zip(summaries_lemmatized[1], wordfreq1)))
word_count_sorted_1 = sorted(word_count_1.items(), key=lambda kv: kv[1], reverse=True)
df_word_count_1 = pd.DataFrame(data = word_count_sorted_1, columns = ['Word', 'Count']).set_index('Word')

wordfreq2 = []
for word in summaries_lemmatized[2]:
    wordfreq2.append(summaries_lemmatized[2].count(word))

word_count_2 = dict(list(zip(summaries_lemmatized[2], wordfreq2)))
word_count_sorted_2 = sorted(word_count_2.items(), key=lambda kv: kv[1], reverse=True)
df_word_count_2 = pd.DataFrame(data = word_count_sorted_2, columns = ['Word', 'Count']).set_index('Word')

df_word_count_all = df_word_count_1.merge(df_word_count_2, 
                                on='Word', how='outer').sum(axis=1)


# remove generic words
words_to_remove = ['is', 'a', 'the', 'and', 'our', 'are', 'this', 
                   'with', 'and', 'you', 'your', 'to', 'of', 'in']





# split into words
listings_text6 = [line.split() for line in listings_text5]

# count frequency of words
from collections import Counter
counts = [Counter(line) for line in listings_text6]

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


