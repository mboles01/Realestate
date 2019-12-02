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
