# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:26:33 2019

@author: BolesMi
"""

# set up working directory
import os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
#os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import data
filename = 'data_all_2.csv'

import csv
with open(filename, mode='r') as f:
    reader = csv.reader(f, delimiter=',')
    data_all = [row for row in reader]
    addresses = [i[1] + str(' ') + i[2] + str(' CA ') + i[3] for i in data_all][1:]
f.close()

# loop over addresses, find lat/long coordinates
from geopy.geocoders import Nominatim
import time
geolocator = Nominatim(user_agent="Mozilla/5.0", timeout = 10)

address_lat = []
address_long = []
for counter, address in enumerate(addresses[4253:],1):
    location = geolocator.geocode(address)
    try:
        lat = location.latitude
    except:
        lat = 0
    try:
        long = location.longitude
    except:
        long = 0
    address_lat.append(lat)
    address_long.append(long)
    print('Getting coordinates for entry %s of %s' % (counter,len(addresses[4253:])))
    time.sleep(1)    


# create dataframe of longitude and latitudes, append to full data set and resave
import pandas as pd
data_all2 = pd.read_csv('data_all_2.csv')

d = {'Longitude': address_long, 'Latitude': address_lat}
latlong = pd.DataFrame(data=d)
data_with_coords = data_all2.join(latlong)

## gather coordinates from subset of full data set
#latlong.index = range(4253,4850)
#data_subset = data_all2[4253:]

# write .csv file with data
data_with_coords.to_csv('data_with_coords.csv')

