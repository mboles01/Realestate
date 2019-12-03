#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 15:25:32 2019

@author: michaelboles
"""

# split and lemmatize text
import nltk
w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()

def lemmatize_text(text):
    return [lemmatizer.lemmatize(w) for w in w_tokenizer.tokenize(text)]

# create word frequency dictionary across all listings and sort
def count_words(text):
    wordcount = {}
    for row in text:
        for word in row:        
            if not word in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] = wordcount[word] + 1
    return wordcount

# remove stop words 
from nltk.corpus import stopwords
def remove_stopwords(text):
    stop_words = stopwords.words('english')
    new_text = []
    for word in text:
        if word not in stop_words:
            new_text.append(word)
    return(new_text)

# remove single characters
def remove_singlechar(text):
    new_text = []
    for word in text:
        if len(word) > 1:
           new_text.append(word)
    return(new_text)