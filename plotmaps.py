# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:36:29 2019

@author: BolesMi
"""

# set up working directory
import os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac

# import plot functions
from cartoplotfunctions import cartoplot_bay, cartoplot_sf, cartoplot_eastbay, cartoplot_southbay

# import data, create plots
import pandas as pd
data_with_coords = pd.read_csv('data_with_coords_to_4253.csv')
long = data_with_coords.loc[:,"Longitude"]
lat = data_with_coords.loc[:,"Latitude"]
color = data_with_coords.loc[:,"Price"]
mincolor = 750000; maxcolor = 3000000; size = 20

cartoplot_bay(long, lat, color, mincolor, maxcolor, size)
cartoplot_sf(long, lat, color, mincolor, maxcolor, size)
cartoplot_eastbay(long, lat, color, mincolor, maxcolor, size)
cartoplot_southbay(long, lat, color, mincolor, maxcolor, size)
