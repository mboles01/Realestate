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
listings_1[['extra_people','price','cleaning_fee','security_deposit']] = listings_1[['extra_people','price','cleaning_fee','security_deposit']].replace('[\$,]', '', regex=True).astype(float)

## convert 'last review' column from string to date time
#listings_1['last_review'] = pd.to_datetime(listings_1['last_review'])

# remove outliers: > 5 beds, > 4 baths, > $1000/night
listings_2 = listings_1[(listings_1['bedrooms'] < 5) & (listings_1['bathrooms'] < 4) & (listings_1['bathrooms'] < 4) & (listings_1['price'] < 1000)]

# exclude hotels, listings with zero bookings
listings_3 = listings_2[(listings_2['property_type'] != 'Hotel') & (listings_2['number_of_reviews'] != 0)]

# CREATE REVENUE ESTIMATE



