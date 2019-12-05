#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 16:43:36 2019

@author: michaelboles
"""

# set up working directory
import sys
import os
#os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate/Data/ABB') # Mac
os.chdir('/Users/bolesmi/Lam/Coding/Python/2019/Realestate/Data/ABB') # PC

# import standard packages
import numpy as np
import pandas as pd

# add additional path to get nlp functions
sys.path.append('./Scripts')

# import cleaned SF listing dataset with text descriptions
listings_sf_clean = pd.read_csv('./Data/Clean/San_Francisco/listings_sf_data_clean_full.csv')

listings_sf_clean_text = listings_sf_clean[['id', 'name', 'host_name',
                                    'summary', 'space', 'description',
                                    'neighborhood_overview', 'notes', 'transit', 
                                    'access', 'interaction', 'house_rules', 
                                    'monthly_revenue', 'revenue_category']]

### TEXT CLEANING ###

# replace NaNs with empty string
listings_text1 = listings_sf_clean_text.replace(np.nan, '', regex=True)

# replace punctuation with spaces
import string
listings_text2 = listings_text1.replace('['+string.punctuation+']', ' ', regex=True)

# make all lowercase
listings_text3 = listings_text2.apply(lambda x: x.astype(str).str.lower())

# within a single listing, combine text across all text fields
listings_text4 = listings_text3.copy()

listings_text4['Combined text'] = listings_text4[['name', 'summary', 'space', 'description', 
              'neighborhood_overview', 'notes', 'transit', 'access', 'interaction', 
              'house_rules']].apply(lambda x: '\n \n'.join(x), axis=1)

# split and lemmatize text for columns of interest: name, summary, space, description
from nlp_functions import lemmatize_text
listings_text5 = listings_text4['Combined text'].apply(lemmatize_text)

# remove stopwords
from nlp_functions import remove_stopwords        
listings_text6 = listings_text5.apply(lambda x: remove_stopwords(x))

# remove single characters
from nlp_functions import remove_singlechar        
listings_text7 = listings_text6.apply(lambda x: remove_singlechar(x))

# remove words that contain a number
from nlp_functions import remove_numbers        
listings_text8 = listings_text7.apply(lambda x: remove_numbers(x))

# remove words that contain non-Latin characters
from nlp_functions import remove_nonlatin
listings_text9 = listings_text8.apply(lambda x: remove_nonlatin(x))


### CREATE BAG OF WORDS ### 

# create simple bag of words vector for listing text
from sklearn.feature_extraction.text import CountVectorizer
vectorizer_bow = CountVectorizer()
corpus = listings_text9.apply(lambda x: ' '.join(x))
bagofwords = vectorizer_bow.fit_transform(corpus).toarray()
bagofwords_labeled = pd.DataFrame(data = bagofwords, columns = vectorizer_bow.get_feature_names())

# create tf-idf (term frequency - inverse document frequency) vector for listing text
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer_tfidf = TfidfVectorizer()
tfidf = vectorizer_tfidf.fit_transform(corpus).toarray()
tfidf_labeled = pd.DataFrame(data = tfidf, columns = vectorizer_tfidf.get_feature_names())

# recombine numerical listing data with bag of words vector
selected = listings_sf_clean_text[['id', 'name', 'monthly_revenue', 'revenue_category']]
listings_bow = pd.concat([selected, bagofwords_labeled], axis=1)
listings_tfidf = pd.concat([selected, tfidf_labeled], axis=1)

# write .csv file with data
listings_bow.to_csv('.\Data\Clean\San_Francisco\listings_sf_data_bow.csv', 
                    index=False, compression='gzip')

listings_tfidf.to_csv('.\Data\Clean\San_Francisco\listings_sf_data_tfidf.csv', 
                    index=False, compression='gzip')

