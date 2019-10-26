#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:25:15 2019

@author: michaelboles
"""

# set up working directory
import os
#os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate/Data/ABB/Data/San Francisco') # Mac
os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate\\Data\ABB') # PC

# import packages
import pandas as pd

# import SF calendar dataset
calendar_raw = pd.read_csv('.\Data\San_Francisco\calendar_1.csv')

# get column names 
calendar_colnames = list(calendar_raw)

# get columns of interest: 
calendar_1 = calendar_raw[['listing_id', 'date', 'available','price']].copy()

# CLEAN DATA

# convert prices from string '$__' to float
calendar_1[['price']] = calendar_1[['price']].replace('[\$,]', '', regex=True).astype(float)




