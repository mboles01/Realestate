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
data_temp = pd.read_csv('data_clean.csv')

# drop second column - extra index
data = data_temp.drop(['Unnamed: 0'], axis = 1)

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

### switch to pandas? ###

# do analogous queries in pandas
rockridge = data.loc[data['Zip'] == 94618]

# set latitude, longitude window for bay, sf, south bay, east bay








