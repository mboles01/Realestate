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

# add zipcode to base url
zipcode = zipcodes[5]
baseurl = 'https://www.realtor.com/realestateandhomes-search/'
url = baseurl + zipcode

# connect to Realtor, obtain addresses and prices
url = 'https://www.realtor.com/realestateandhomes-search/94618'
session = requests.Session()
homepage = session.get(url)
tree = html.fromstring(homepage.content)
address = list(map(str, tree.xpath('//span[@class="listing-street-address"]//text()')))
price = list(map(str, tree.xpath('//span[@class="data-price"]//text()')))
# returns empty lists -- why?


# connect to MLS listings, obtain addresses and prices
url = 'https://www.mlslistings.com/Search/Result/4a5c523e-ce21-471d-9350-d2743bd16038/1'
session = requests.Session()
homepage = session.get(url) 
tree = html.fromstring(homepage.content)
address = list(map(str, tree.xpath('//a[@class="search-nav-link"]//text()')))
price = list(map(str, tree.xpath('//span[@class="font-weight-bold listing-price d-block pull-left pr-25"]//text()')))
# succeeds




def webscrape(zipcodes):
    
    # create empty data frame
    data_all = pd.DataFrame()
    
    for counter, zipcode in enumerate(zipcodes,1):
        
        # get homepage session
        session = requests.Session()
        url = "https://www.realtor.com/realestateandhomes-search/94110/type-single-family-home"
        homepage = session.get(url)  # Mac
#        homepage = session.get('https://www.realtor.com/',verify='C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate\\Lam_certificate_Realtor_June2019.cer')
        soup = BeautifulSoup(homepage.content, "html.parser")
        tree = html.fromstring(soup.prettify())

        
        # get security token, post search data
        token = soup.find("input", attrs={"name" : "__RequestVerificationToken"})['value']
        data = {'transactionType': 'buy', 'listing_status': 'Active', 'searchTextType': '', 'searchText': zipcode,'__RequestVerificationToken': token, 'property_type': 'SingleFamilyResidence'}
        search_results = session.post("https://www.mlslistings.com/Search/ResultPost", data=data)
        tree = html.fromstring(search_results.content)
        
        # update status
        print('Scraping data for zipcode (%s/%s): ' % (counter,len(zipcodes)) + str(zipcode))
        
        # scrape desired information
        price_raw = list(map(str, tree.xpath('//span[@class="data-price"]//text()')))
        tree.xpath('//span[@class="data-price"]/text()')


<div title="buyer-name">Carson Busses</div>
<span class="item-price">$29.95</span>
Knowing this we can create the correct XPath query and use the lxml xpath function like this:

    
#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')

        
        
        address_raw = list(map(str, tree.xpath('//a[@class="search-nav-link"]//text()')))
        hometype_raw = list(map(str, tree.xpath('//div[@class="listing-info clearfix font-size-sm line-height-base listing-type mb-25"]//text()')))
        beds_raw = list(map(str, tree.xpath('//span[@class="listing-info-item font-size-sm line-height-base d-block pull-left pr-50 listing-beds"]//text()')))
        baths_raw = list(map(str, tree.xpath('//span[@class="listing-info-item font-size-sm line-height-base d-block pull-left pr-50 listing-baths"]//text()')))
        homesize_raw = list(map(str, tree.xpath('//span[@class="font-weight-bold info-item-value d-block pull-left pr-25"]//text()')))
        lot_raw = list(map(str, tree.xpath('//span[@class="listing-info-item font-size-sm line-height-base d-block pull-left pr-50 listing-lot-size"]//text()')))
        garage_raw = list(map(str, tree.xpath('//span[@class="listing-info-item font-size-sm line-height-base d-block pull-left pr-50 listing-garage"]//text()')))
        yearbuilt_raw = list(map(str, tree.xpath('//span[@class="listing-info-item font-size-sm line-height-base d-block pull-left pr-50 listing-sqft last"]//text()')))
        
        <span class="data-price">$8,600,000</span>
        
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
        
        