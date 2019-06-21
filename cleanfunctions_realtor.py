# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:31:27 2019

@author: BolesMi
"""

# DEFINE DATA CLEANING FUNCTIONS 
import re
import math

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
    try:
        baths = [float(i) for i in baths_raw]
    except:
        baths = re.findall(r'(.+)+', baths_raw)
    return baths


# pull out home size entries, replace hyphens
def homesize_clean(homesize_raw):
    homesize_temp = [re.sub(',','',i) for i in homesize_raw]
    homesize = [int(i) for i in homesize_temp]
    return homesize

# define function to convert between sqft and acres
def acretosqft(lotinsqft):
    return round(lotinsqft*43560,3)

# find lot size, convert sqft values to acres
def lotsize_clean(lotsize_raw, lotunits_raw):
    lotsize_temp1 = [re.sub(',','',i) for i in lotsize_raw]
    lotsize_temp2 = [float(i) for i in lotsize_temp1]
    lotunits_temp2 = []
    lotsize = []
    for line in lotunits_raw: 
        lotunits_temp1 = re.findall(r'\s+(.+)\s+lot', line)
        lotunits_temp2.append(lotunits_temp1)
    lotunits = [i[0] for i in lotunits_temp2]
    for counter, line in enumerate(lotsize_temp2):
        if lotunits[counter] == 'acres':
            lotsize_temp = acretosqft(line)
        else:
            lotsize_temp = line
        lotsize.append(lotsize_temp)
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

