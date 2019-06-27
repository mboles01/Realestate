# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:36:29 2019

@author: michaelboles
"""

# set up working directory
import os
#os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import data, create plots
import pandas as pd
data = pd.read_csv('data_clean.csv')

# calculate quintiles
from calculatequintiles import price_quintiles, pricepersqft_quintiles, priceperlotsqft_quintiles
pricequintiles = price_quintiles(data)
pricepersqftquintiles = pricepersqft_quintiles(data)
priceperlotsqftquintiles = priceperlotsqft_quintiles(data)

# plot maps
from cartoplotfunctions import cartoplot_bay_price, cartoplot_sf_price, cartoplot_bay_pricepersqft, cartoplot_bay_priceperlotsqft
#cartoplot_sf, cartoplot_eastbay, cartoplot_southbay

# bay area overview
mapsize = 30
cartoplot_bay_price(data, mapsize, pricequintiles)
cartoplot_bay_pricepersqft(data, mapsize, pricepersqftquintiles)
cartoplot_bay_priceperlotsqft(data, mapsize, priceperlotsqftquintiles)

# sf 
mapsize = 30
cartoplot_sf_price(data, mapsize, pricequintiles)

# south bay
mapsize = 30
cartoplot_bay_price(data, mapsize, pricequintiles)
cartoplot_bay_pricepersqft(data, mapsize, pricepersqftquintiles)
cartoplot_bay_priceperlotsqft(data, mapsize, priceperlotsqftquintiles)
