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
    
# remove 'words' that with numbers 
import re
def remove_numbers(text):
    numbers = re.compile(r'(\d+)|(\S+\d+)') # starts with number or contains number
    not_numbers = [line for line in text if not numbers.match(line)]
    return(not_numbers)

# remove non-latin characters
def remove_nonlatin(text):
#    chinese = re.compile(r'[\u4e00-\u9fff]+') # 4E00—9FFF range covers Chinese, Japanese, and Korean 
    regex_latin = re.compile(r'[\u0020-\u007f]+') # this range covers basic Latin characters
    latin = [line for line in text if regex_latin.match(line)]
#    not_chinese = [line for line in text if not chinese.match(line)]
    return(latin)
