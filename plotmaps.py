# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:36:29 2019

@author: michaelboles
"""

# set up working directory
import os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
#os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

### Bay overview ###

# import data
import pandas as pd
data_bay = pd.read_csv('./data/data_bay.csv')

# calculate quintiles
from calculatequintiles import price_quintiles
pricequintiles_bay = price_quintiles(data_bay)

# plot data
from cartoplotfunctions import cartoplot_bay_price
mapsize = 30
cartoplot_bay_price(data_bay, mapsize, pricequintiles_bay)


### San Francisco ###

# import data
data_sf = pd.read_csv('./data/data_sf.csv')

# calculate quintiles
pricequintiles_sf = price_quintiles(data_sf)

# plot data
from cartoplotfunctions import cartoplot_sf_price
mapsize = 15
cartoplot_sf_price(data_sf, mapsize, pricequintiles_sf)


### East Bay ###

# import data
data_eastbay = pd.read_csv('./data/data_eastbay.csv')

# calculate quintiles
pricequintiles_eastbay = price_quintiles(data_eastbay)

# plot data
from cartoplotfunctions import cartoplot_eastbay_price
mapsize = 15
cartoplot_eastbay_price(data_eastbay, mapsize, pricequintiles_eastbay)

### Peninsula ###

# import data
data_peninsula = pd.read_csv('./data/data_peninsula.csv')

# calculate quintiles
pricequintiles_peninsula = price_quintiles(data_peninsula)

# plot data
from cartoplotfunctions import cartoplot_peninsula_price
mapsize = 15
cartoplot_peninsula_price(data_peninsula, mapsize, pricequintiles_peninsula)


### South Bay ###

# import data
data_southbay = pd.read_csv('./data/data_southbay.csv')

# calculate quintiles
pricequintiles_southbay = price_quintiles(data_southbay)

# plot data
from cartoplotfunctions import cartoplot_southbay_price
mapsize = 15
cartoplot_southbay_price(data_southbay, mapsize, pricequintiles_southbay)







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
