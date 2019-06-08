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
for counter, address in enumerate(addresses,1):
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
    print('Getting coordinates for entry %s of %s' % (counter,len(addresses)))
    time.sleep(1)    


# create dataframe of longitude and latitudes, append to full data set and resave
import pandas as pd
data_all2 = pd.read_csv('data_all_2.csv')

d = {'Longitude': address_long, 'Latitude': address_lat}
latlong = pd.DataFrame(data=d)

data_subset = data_all2[0:4253]

data_with_coords = data_subset.join(latlong)

# write .csv file with data
data_with_coords.to_csv('data_with_coords_to_4253.csv')








# Create a Stamen terrain background instance.
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt

stamen_terrain = cimgt.Stamen('terrain-background')
fig = plt.figure(figsize = (10,10))
# Create a GeoAxes in the tile's projection.
ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
# Limit the extent of the map to a small longitude/latitude range.
ax.set_extent([-122.7, -121.5, 37.15, 38.15], crs=ccrs.Geodetic())
# Add the Stamen data at zoom level 8.
ax.add_image(stamen_terrain, 12)
    
ax.scatter(data_with_coords.loc[:,"Longitude"], data_with_coords.loc[:,"Latitude"], s=5, c='r',transform=ccrs.PlateCarree())
plt.show()








    

print(location.address)
print((location.latitude, location.longitude))
print(location.raw)




# try google api
from geopy import geocoders
g = geocoders.GoogleV3(api_key='AIzaSyAhFM1oWVQ7U_YnpOmMMI9v4s19DUBD1JY')
location = g.geocode(address, timeout=10)
