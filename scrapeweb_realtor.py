# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:45:56 2019

@author: BolesMi
"""

# set up working directory
import os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac


# import data cleaning functions
from cleandata_realtor import address_clean, beds_clean, baths_clean, homesize_clean, lotsize_clean, price_clean, coords_clean

# import modules
from lxml import html
import requests
from user_agent import generate_user_agent
import pandas as pd
import time
from bs4 import BeautifulSoup
import re


def webscrape(zipcodes):
    
    # create empty data frame
    data_all = pd.DataFrame()
    
    for counter, zipcode in enumerate(zipcodes,1):
        
        # get homepage session
        url = 'https://www.realtor.com/realestateandhomes-search/' + zipcode + '/beds-1/baths-1/type-single-family-home'
        session = requests.Session()
        headers = {'User-Agent': generate_user_agent()}
        homepage = session.get(url, timeout = 5, headers = headers)
        tree = html.fromstring(homepage.content)
#        soup = BeautifulSoup(homepage.content, "html.parser")
        
        # update status
        print('Scraping data for zipcode (%s/%s): ' % (counter,len(zipcodes)) + str(zipcode))
        
        # find number of results returned
        resultcount_temp = tree.xpath('//span[@id="search-result-count"]//text()')
        if resultcount_temp:
            resultcount = int(re.findall(r'\s+(\d+)', resultcount_temp[0])[0])
            print('%s results found for zipcode %s' % (resultcount, zipcode))
        else:
            print('No results found for zipcode %s' % zipcode)
            continue
        #        noresults = tree.xpath('//h3[@class="no-result-subtitle"]//text()')

        
        # scrape desired information
        address_raw = list(map(str, tree.xpath('//span[@class="listing-street-address"]//text()')))
        city = list(map(str, tree.xpath('//span[@class="listing-city"]//text()')))
        state = list(map(str, tree.xpath('//span[@class="listing-region"]//text()')))
        zip_code = list(map(str, tree.xpath('//span[@class="listing-postal"]//text()')))
        price_raw = list(map(str, tree.xpath('//span[@class="data-price"]//text()')))
        beds_raw = list(map(str, tree.xpath('//span[@class="data-value meta-beds"]//text()')))
        baths_raw = list(map(str, tree.xpath('//li[@data-label="property-meta-baths"]//span[@class="data-value"]//text()')))
        homesize_raw = list(map(str, tree.xpath('//li[@data-label="property-meta-sqft"]//span[@class="data-value"]//text()')))
        lotsize_raw = list(map(str, tree.xpath('//li[@data-label="property-meta-lotsize"]//span[@class="data-value"]//text()')))
        lotunits_raw = list(map(str, tree.xpath('//li[@data-label="property-meta-lotsize"]//span[@class="lot-label"]//text()')))
        coords_raw = list(map(str, tree.xpath('//span[@class="listing-geo"]//@content')))
        
                                                
        # clean raw data
        address = address_clean(address_raw)
        beds = beds_clean(beds_raw)
        baths = baths_clean(baths_raw)
        homesize = homesize_clean(homesize_raw)
        lotsize = lotsize_clean(lotsize_raw, lotunits_raw)
        price = price_clean(price_raw)
        latitude, longitude = coords_clean(coords_raw)
        
        # count up lengths of arrays to be joined
        len_address = 'Address', len(address)
        len_city = 'City', len(city)
        len_state = 'State', len(state)
        len_zip = 'Zip', len(zip_code)
        len_beds = 'Beds', len(beds)
        len_baths = 'Baths', len(baths)
        len_homesize = 'Homesize', len(homesize)
        len_lotsize = 'Lot', len(lotsize)
        len_price = 'Price', len(price)
        len_latitude = 'Latitude', len(latitude)
        len_longitude = 'Longitude', len(longitude)
        
        # check if any are not matching the others     
        lengths = [len_address, len_city, len_state, len_zip, len_beds, len_baths, len_homesize, len_lotsize, len_price, len_latitude, len_longitude]
        len_proper = max(set([item[1] for item in lengths]), key=[item[1] for item in lengths].count)
        for counter, item in enumerate(lengths):
            if item[1] != len_proper:
                print('%s has improper length: %s, should be %s' % (lengths[counter][0], lengths[counter][1], len_proper))
                pass
#                return address, city, zip_code, beds, baths, homesize, lot, yearbuilt, garage, hometype, price, address_raw, beds_raw, baths_raw, lot_raw, yearbuilt_raw, garage_raw, hometype_raw, price_raw
#                sys.exit()
            else:
                pass
        
        # create data frame from scraped, cleaned data
        try:
            data_temp = {'Address': address, 'City': city, 'State': state, 
                         'Zip': zip_code, 'Beds': beds, 'Baths': baths, 
                         'Home size': homesize, 'Lot size': lotsize, 'Price': price,
                         'Latitude': latitude, 'Longitude': longitude}
        
            dataframe_temp = pd.DataFrame(data_temp)
            data_all = data_all.append(dataframe_temp)
        except:
            print('Zipcode %s was skipped' % zipcode)
        
        # wait, then scrape next zipcode
        time.sleep(1)
        
    return data_all
        
        