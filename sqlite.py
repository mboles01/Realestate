#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 12:38:50 2019

@author: michaelboles
"""

# set up working directory
import os
#os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import data
import pandas as pd
data = pd.read_csv('data_clean.csv')

# remind myself what the column names are
data.columns

## create in-memory sqlite database, add dataframe
#from sqlalchemy import create_engine
#engine = create_engine('sqlite://', echo = False)
#data.to_sql('Realestate', con=engine)
#
## query database
#engine.execute("SELECT * FROM Realestate").fetchall() # gets everything
#engine.execute('SELECT * FROM Realestate WHERE Zip = 94618').fetchall() # matches a zipcode
#
## create a list from sql query 
## returns list of rowproxy objects, omits column names - why is this so hard
#rockridge = engine.execute('SELECT * FROM Realestate WHERE Zip = 94618').fetchall() # matches a zipcode

### switch to pandas? ###

# set latitude, longitude window for bay, sf, south bay, east bay
data_bay = data.query('-122.7 < Longitude < -121.5 and 37.15 < Latitude < 38.15')
data_sf = data.query('-122.55 < Longitude < -122.35 and 37.7 < Latitude < 37.825')
data_eastbay = data.query('-122.35 < Longitude < -122.025 and 37.75 < Latitude < 37.925')
data_southbay = data.query('-122.15 < Longitude < -121.75 and 37.2 < Latitude < 37.45')

# save data sets
data_bay.to_csv('data_bay.csv')
data_sf.to_csv('data_sf.csv')
data_eastbay.to_csv('data_eastbay.csv')
data_southbay.to_csv('data_southbay.csv')
