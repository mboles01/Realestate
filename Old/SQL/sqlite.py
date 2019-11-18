#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 12:38:50 2019

@author: michaelboles
"""

# set up working directory
import os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
#os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import data
import pandas as pd
data = pd.read_csv('./Data/listings/data_all_price_predictions.csv')

# remind myself what the column names are
data.columns

# create in-memory sqlite database, add dataframe
from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo = False)
data.to_sql('Realestate', con=engine)

# query database
engine.execute("SELECT * FROM Realestate").fetchall() # gets everything
engine.execute('SELECT * FROM Realestate WHERE Zip = 94618').fetchall() # matches a zipcode

# create a list from sql query 
# returns list of rowproxy objects, omits column names - why is this so hard
rockridge = engine.execute('SELECT * FROM Realestate WHERE Zip = 94618').fetchall() # matches a zipcode
