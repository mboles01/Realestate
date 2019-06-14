# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:45:56 2019

@author: BolesMi
"""

# import data cleaning functions
from cleandata import address_clean, beds_clean, baths_clean, homesize_clean, lot_clean, yearbuilt_clean, garage_clean

# import modules
from bs4 import BeautifulSoup
from lxml import html
import requests
import pandas as pd
import time

def webscrape(zipcodes):
    
    # create empty data frame
    data_all = pd.DataFrame()
    
    for counter, zipcode in enumerate(zipcodes,1):
        
        # get homepage session
        url = 'https://www.realtor.com/realestateandhomes-search/94618/type-single-family-home'
        session = requests.Session()
        homepage = session.get(url,verify='C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate\\Lam_certificate_Realtor_June2019.cer')
        tree = html.fromstring(homepage.content)
        soup = BeautifulSoup(homepage.content)
        p = soup.prettify()
        
        # update status
        print('Scraping data for zipcode (%s/%s): ' % (counter,len(zipcodes)) + str(zipcode))
        
        # scrape desired information
        address_raw = list(map(str, tree.xpath('//span[@class="listing-street-address"]//text()')))
        city_raw = list(map(str, tree.xpath('//span[@class="listing-city"]//text()')))
        state_raw = list(map(str, tree.xpath('//span[@class="listing-region"]//text()')))
        zipcode_raw = list(map(str, tree.xpath('//span[@class="listing-postal"]//text()')))
        price_raw = list(map(str, tree.xpath('//span[@class="data-price"]//text()')))
        beds_raw = list(map(str, tree.xpath('//span[@class="data-value meta-beds"]//text()')))
        baths_raw = list(map(str, tree.xpath('//li[@data-label="property-meta-baths"]//span[@class="data-value"]//text()')))
        homesize_raw = list(map(str, tree.xpath('//li[@data-label="property-meta-sqft"]//span[@class="data-value"]//text()')))
        lotsize_raw = list(map(str, tree.xpath('//li[@data-label="property-meta-lotsize"]//span[@class="data-value"]//text()')))
        garage_raw = list(map(str, tree.xpath('//li[@data-label="property-meta-garage"]//span[@class="data-value"]//text()')))
        
        # clean raw data
        import re
        address, city, zip_code = address_clean(address_raw)
        beds = beds_clean(beds_raw)
        baths = baths_clean(baths_raw)
        homesize = homesize_clean(homesize_raw)
        lot = lot_clean(lot_raw)
        yearbuilt = yearbuilt_clean(yearbuilt_raw)
        garage = garage_clean(garage_raw)
        hometype = re.findall(r'\s\s(\w+\s\w+\s\w+)',str(hometype_raw))
        price = list(map(int, [re.sub('[$,]','',i) for i in price_raw]))
        
        # count up lengths of arrays to be joined
        len_address = 'Address', len(address)
        len_city = 'City', len(city)
        len_zip = 'Zip', len(zip_code)
        len_beds = 'Beds', len(beds)
        len_baths = 'Baths', len(baths)
        len_homesize = 'Homesize', len(homesize)
        len_lot = 'Lot', len(lot)
        len_yearbuilt = 'Year built', len(yearbuilt)
        len_garage = 'Garage', len(garage)
        len_hometype = 'Home type', len(hometype)
        len_price = 'Price', len(price)
        
        # check if any are not matching the others     
        lengths = [len_address, len_city, len_zip, len_beds, len_baths, len_homesize, len_lot, len_yearbuilt, len_garage, len_hometype, len_price]
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
            data_temp = {'Address': address, 'City': city, 'Zip': zip_code, 
                     'Beds': beds, 'Baths': baths, 'Home size': homesize, 
                     'Lot size': lot, 'Year built': yearbuilt, 'Garage': garage, 
                     'Home type': hometype, 'Price': price}
        
            dataframe_temp = pd.DataFrame(data_temp)
            data_all = data_all.append(dataframe_temp)
        except:
            print('Zipcode %s was skipped' % zipcode)
        
        # wait, then scrape next zipcode
        time.sleep(1)
        
    return data_all
        
        