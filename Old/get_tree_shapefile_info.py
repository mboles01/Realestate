#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 17:40:13 2019

@author: michaelboles
"""

# set up working directory
import os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
#os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

import geopandas as gpd
shapefile = './shapefiles/Tree coverage/CtySubdiv.shp'
#shapefile = r'./shapefiles/Bay Zips/ZIPCODE.shp'
shapefile_info = gpd.read_file(r'./shapefiles/Tree coverage/CtySubdiv.shp')
