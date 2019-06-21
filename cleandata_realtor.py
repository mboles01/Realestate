# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:57:21 2019

@author: BolesMi
"""

# set up working directory
import os
#os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import full (raw) data set
import pandas as pd
filename = 'data_raw.csv'
data_raw = pd.read_csv(filename)

# get data not needing cleaning
city = data_raw['City']
state = data_raw['State']
zipcode = data_raw['Zip']
latitude = data_raw['Latitude']
longitude = data_raw['Longitude']

# clean raw data
from cleanfunctions_realtor import address_clean, beds_clean, baths_clean, homesize_clean, lotsize_clean, price_clean
address = address_clean(data_raw['Address'])
beds = beds_clean(data_raw['Beds'])
baths = baths_clean(data_raw['Baths'])
homesize = homesize_clean(data_raw['Home size'])
lotsize = lotsize_clean(data_raw['Lot size'])
price = price_clean(data_raw['Price'])

# rejoin with cleaned data
data_clean_temp = {'Address': address, 'City': city, 'State': state, 'Zip': zipcode, 
                     'Price': price, 'Beds': beds, 'Baths': baths, 
                     'Home size': homesize, 'Lot size': lotsize,  
                     'Latitude': latitude, 'Longitude': longitude}

data_clean = pd.DataFrame(data_clean_temp)#, index = [order])

# save new csv
data_clean.to_csv('data_clean.csv')


