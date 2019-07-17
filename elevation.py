# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:28:37 2019

@author: BolesMi
"""

# set up working directory
import os
#os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import packages
import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import html
from user_agent import generate_user_agent


# import dataset with lat, long coordinates
data_bay = pd.read_csv('./data/data_bay.csv')
data_bay.columns

lat = data_bay.iloc[111]['Latitude']
long = data_bay.iloc[111]['Longitude']
search = str(lat) + ',' + str(long)

# script for returning elevation from lat, long, based on open elevation data
# which in turn is based on SRTM
#def get_elevation(lat, long):
#    query = ('https://api.open-elevation.com/api/v1/lookup'
#             f'?locations={lat},{long}')
#    r = requests.get(query).json()  # json object, various ways you can extract value
#    # one approach is to use pandas json functionality:
#    elevation = pd.io.json.json_normalize(r, 'results')['elevation'].values[0]
#    return elevation

# loop over latitude/longitude, get elevations
#from elevation import get_elevation

# not working, or very slow

elevation = []
for counter, row in enumerate(data_bay[0:19].iterrows(),1):
    lat = row[1]['Latitude'] #lat = data_bay.loc[0]['Latitude'] 
    long = row[1]['Longitude'] #long = data_bay.loc[0]['Longitude'] 
    url = 'https://api.open-elevation.com/api/v1/lookup?locations=' + str(lat) + ',' + str(long)
    r = requests.get(url, timeout = 100).json()  # json object, various ways you can extract value
    elevation_temp = pd.io.json.json_normalize(r, 'results')['elevation'].values[0]
    elevation.append(elevation_temp)
    if counter % 10 == 0:
        elevation.to_csv('elevation_bay.csv')


# try https://www.whatismyelevation.com/ 

# get homepage session
session = requests.Session()
homepage = session.get('https://www.whatismyelevation.com/')  # Mac
soup = BeautifulSoup(homepage.content, "html.parser")

# 

# get security token, post search data
token = soup.find("input", attrs={"name" : "__RequestVerificationToken"})['value']
data = {'transactionType': 'buy', 'listing_status': 'Active', 'searchTextType': '', 'searchText': zipcode,'__RequestVerificationToken': token, 'property_type': 'SingleFamilyResidence'}
search_results = session.post("https://www.mlslistings.com/Search/ResultPost", data=data)
tree = html.fromstring(search_results.content)

# update status
print('Scraping elevation for address (%s/%s): ' % (counter,len(zipcodes)) + str(zipcode))

# scrape desired information
tree.xpath('//div[@id="elevation"]//text()')



