# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:26:33 2019

@author: BolesMi
"""

# set up working directory
import os
#os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import data
filename = 'data_all.csv'

import csv
with open(filename, mode='r') as f:
    reader = csv.reader(f, delimiter=',')
    data_all = [row for row in reader]
    addresses = [i[1] + str(' ') + i[2] + str(' CA ') + i[3] for i in data_all][1:]
f.close()

# or import csv as pandas dataframe?
import pandas as pd
data_all2 = pd.read_csv('data_all.csv')

# loop over addresses, find lat/long coordinates
from geopy.geocoders import Nominatim
import time
geolocator = Nominatim(user_agent="Mozilla/5.0", timeout = 10)

address_lat = []
address_long = []
for address in addresses[:99]:
    location = geolocator.geocode(address)
    try:
        lat = location.latitude
    except:
        lat = ''
    try:
        long = location.longitude
    except:
        long = ''
    address_lat.append(lat)
    address_long.append(long)
    time.sleep(1)    



data_part = data_all[1:100]



print(location.address)
print((location.latitude, location.longitude))
print(location.raw)
