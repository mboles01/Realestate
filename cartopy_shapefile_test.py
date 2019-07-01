#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 10:32:02 2019

@author: michaelboles
"""


# set up working directory
import os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac

# import functions
import matplotlib.pyplot as plt
import cartopy.io.img_tiles as cimgt
import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature

# Create a Stamen terrain background instance
stamen_terrain = cimgt.Stamen('terrain-background')
fig = plt.figure(figsize = (10, 10))
ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)

# Set range of map, stipulate zoom level
ax.set_extent([-122.7, -121.5, 37.15, 38.15], crs=ccrs.Geodetic())
ax.add_image(stamen_terrain, 12, zorder = 0)

# Add city borders - not working
filename = r'./shapefile/ba_cities.shp' # from https://earthworks.stanford.edu/catalog/stanford-vj593xs7263
shape_feature = ShapelyFeature(Reader(filename).geometries(), ccrs.Geocentric(), edgecolor='black')
ax.add_feature(shape_feature, zorder = 1)
plt.show()