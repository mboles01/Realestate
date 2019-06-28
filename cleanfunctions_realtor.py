# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:31:27 2019

@author: BolesMi
"""

# DEFINE DATA CLEANING FUNCTIONS 
import re
import math
import pandas as pd

# from full address, pull out street address, city, and zipcode 
def address_clean(address_raw):
    address_temp2 = []
#    address = ['']
    for line in address_raw:
        try:
            address_temp1 = re.findall(r'\s+(.+),', line)
        except:
            if math.isnan(line):
                address_temp1 = ['']
        address_temp2.append(address_temp1)
    address = [i[0] for i in address_temp2]
    return address


# find beds, remove hyphens
def beds_clean(beds_raw):
    beds = [int(i) for i in beds_raw]
    return beds
 

# need to remove whitespace, extra text, and convert slashes from baths
def baths_clean(baths_raw):
    baths = []
    for row in baths_raw:
        try:
            baths_temp = float(row)
#            baths = [float(i) for i in baths_raw]
        except:
            baths_temp = float(re.findall(r'(\d+\.\d+)+', row)[0])
        baths.append(baths_temp)
    return baths

# pull out home size entries, replace hyphens
def homesize_clean(homesize_raw):
    homesize = []
    for row in homesize_raw:
        try:
            homesize_temp = int(re.sub(',','',row))
        except:
            homesize_temp = row
        homesize.append(homesize_temp)
    return homesize

# define function to convert between sqft and acres
def acretosqft(lotinsqft):
    return round(lotinsqft*43560,3)

# find lot size, convert sqft values to acres
def lotsize_clean(lotsize_raw):
    lotsize_temp2 = []
    for row in lotsize_raw:
        try:
            lotsize_temp1 = int(re.sub(',','',row))
        except:
            lotsize_temp1 = row
        lotsize_temp2.append(lotsize_temp1)
    lotsize = []
    for row in lotsize_temp2:
        if isinstance(row, str):
            lotsize_temp3 = acretosqft(float(row))
        else:
            lotsize_temp3 = row
        lotsize.append(lotsize_temp3)
    return lotsize

def cleanlot(lot_raw):
    lotsize = []
    for row in lot_raw:
        if pd.isnull(row):
            lotsize.append(float('nan'))
        else:
            if row < 300:
                lot_temp = acretosqft(float(row))
            else:
                lot_temp = row
            lotsize.append(lot_temp)
    return lotsize

# remove dollar sign in price
def price_clean(price_raw):
    price = list(map(int, [re.sub('[$,]','',i) for i in price_raw]))
    return price

# get latitude, longitude coordinates
def coords_clean(coords_raw):
    latitude = []; longitude = []
    for counter, line in enumerate(coords_raw):
        if counter % 2 == 0:
            latitude.append(float(line))
        else:
            longitude.append(float(line))
    return latitude, longitude


# pull out first entry in one-entry list, if empty call NaN
def flatten(entry):
    if len(entry) == 0:
        cell = float('nan')
    else:
        cell = entry[0]
    return cell

