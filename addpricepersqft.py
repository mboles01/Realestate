#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 17:05:25 2019

@author: michaelboles
"""

# pull in data frame with appended latitude, longitude coordinates
import pandas as pd
data_full = pd.read_csv('data_with_coords.csv')

# append price per sqft, price per lot sqft to full data set
data_full["Price per sqft"] = data_full["Price"]/data_full["Home size"]
data_full["Price per lot sqft"] = data_full["Price"]/(43560*data_full["Lot size"])

# remove unneeded columns
del data_full['Unnamed: 0']
del data_full['Unnamed: 0.1']
del data_full['Home type']

# remove unneeded rows
data_full = data_full[data_full["City"] != "Manhattan Beach"]

# write .csv file with data
data_full.to_csv('data_full.csv')
