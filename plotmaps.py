# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:36:29 2019

@author: BolesMi
"""

# import plot functions
from plotfunctions import cartoplot_bay, cartoplot_sf, cartoplot_eastbay, cartoplot_southbay

# import data, create plots
import pandas as pd
data_with_coords = pd.read_csv('data_with_coords.csv')
long = data_with_coords.loc[:,"Longitude"]
lat = data_with_coords.loc[:,"Latitude"]
color = data_with_coords.loc[:,"Price"]
mincolor = 1000000; maxcolor = 3000000

cartoplot_bay(long, lat, color, mincolor, maxcolor)
cartoplot_sf(long, lat)
cartoplot_eastbay(long, lat)
cartoplot_southbay(long, lat)
