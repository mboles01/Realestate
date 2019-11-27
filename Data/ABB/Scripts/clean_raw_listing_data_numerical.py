#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:25:15 2019

@author: michaelboles
"""

# set up working directory
import os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate/Data/ABB') # Mac

# import packages
import pandas as pd

# import SF listings dataset
listings_raw = pd.read_csv('./Data/Raw/San_Francisco/listings_2.csv')

# get column names 
listings_colnames = list(listings_raw)

# get columns of interest: 
    
listings_1 = listings_raw[['id', 'name', 'host_name',
                         'neighbourhood', 'latitude', 'longitude',
                         'bedrooms', 'bathrooms', 'square_feet', 
                         'property_type', 'room_type',
                         'guests_included', 'extra_people', 'minimum_nights',
                         'availability_30', 'availability_90', 'availability_365',
                         'number_of_reviews', 'review_scores_rating', 'last_review', 
                         'reviews_per_month',
                         'price', 'cleaning_fee', 'security_deposit']].copy()

# CLEAN DATA

# convert prices from string '$__' to float
listings_1[['extra_people','price','cleaning_fee','security_deposit']] = listings_1[['extra_people','price','cleaning_fee','security_deposit']].replace('[\$,]', '', regex=True).astype(float)

# convert 'last review' column from string to date time
listings_1['last_review'] = pd.to_datetime(listings_1['last_review'])

# remove outliers: > 5 beds, > 4 baths, > $1000/night
listings_2 = listings_1[(listings_1['bedrooms'] < 5) & (listings_1['bathrooms'] < 4) & (listings_1['bathrooms'] < 4) & (listings_1['price'] < 1000)]

# exclude hotels, listings with zero bookings
listings_3 = listings_2[(listings_2['property_type'] != 'Hotel') & (listings_2['number_of_reviews'] != 0)]

# exclude listings that have not been reviewed in the last 6 months (for data from 10/14, use 4/14)
listings_4 = listings_3[(listings_3['last_review'] > '2019-04-14')]

# replace blanks with zeros in cleaning fee, security deposit columns
listings_5 = listings_4.copy()
listings_5[['cleaning_fee','security_deposit']] = listings_5[['cleaning_fee','security_deposit']].fillna(0)

# CREATE REVENUE ESTIMATE

# assume 50% of bookings result in a review and average booking is 5.5 nights
# revenue/month = (reviews/month)*(2 bookings/review)*(5.5 nights/booking)*(nightly price)

listings_6 = listings_5.copy()
listings_6['monthly_revenue'] = 11*listings_5['reviews_per_month']*listings_5['price'] 

# write .csv file with data
listings_6.to_csv('.\Data\Clean\San_Francisco\listings_sf_data_clean_full.csv', index=False)






