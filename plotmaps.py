# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:36:29 2019

@author: BolesMi
"""

# set up working directory
import os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac

# import data, create plots
import pandas as pd
data_full = pd.read_csv('data_full.csv')

# calculate quintiles
from calculatequintiles import price_quintiles, pricepersqft_quintiles, priceperlotsqft_quintiles
pricequintiles = price_quintiles(data_full)
pricepersqftquintiles = pricepersqft_quintiles(data_full)
priceperlotsqftquintiles = priceperlotsqft_quintiles(data_full)

# plot maps
from cartoplotfunctions import cartoplot_bay_price, cartoplot_bay_pricepersqft, cartoplot_bay_priceperlotsqft
#cartoplot_sf, cartoplot_eastbay, cartoplot_southbay

mapsize = 30
cartoplot_bay_price(data_full, mapsize, pricequintiles)
cartoplot_bay_pricepersqft(data_full, mapsize, pricepersqftquintiles)
cartoplot_bay_priceperlotsqft(data_full, mapsize, priceperlotsqftquintiles)

