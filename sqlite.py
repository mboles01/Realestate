#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 12:38:50 2019

@author: michaelboles
"""

# set up working directory
import  os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
#os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import data
import pandas as pd
data = pd.read_csv('data_clean.csv')

# drop second column
data2 = data.drop(['Unnamed: 0'], axis = 1)

# sqlite 3
import sqlite3 
conn = sqlite3.connect('data.db')
data.to_sql(data, conn, if_exists='append', index=False)


import csv, sqlite3
conn_memory = sqlite3.connect(":memory:")
cur = conn_memory.cursor()
cur.execute("CREATE TABLE data ('Address','City','State','Zip','Price','Beds','Baths','Home size','Lot size','Latitude','Longitude')") 

with open('data_clean.csv','rt') as fin: 
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['Address'], i['City']) for i in dr]

cur.executemany("INSERT INTO data (Address, City) VALUES (?, ?);", to_db)
conn.commit()
conn.close()

cur.execute("SELECT * FROM data")
rows = cur.fetchall()
for row in rows:
    print(row)