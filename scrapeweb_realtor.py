# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:45:56 2019

@author: BolesMi
"""

## set up working directory
#import os
##os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
#os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import modules
from lxml import html
import requests
from user_agent import generate_user_agent
import pandas as pd
import numpy.random as npr
import time
import re
from collections import OrderedDict
from cleanfunctions_realtor import flatten, acretosqft
from getip import get_proxies
from itertools import cycle

# define webscraping function

def webscrape(zipcodes):
    
    # create empty data frame
    data_all = pd.DataFrame()
    
    for counter, zipcode in enumerate(zipcodes,1):
        
        # build in wait time
        wait_time = npr.randint(1,6)
        time.sleep(wait_time)

        # get homepage session
        url = 'https://www.realtor.com/realestateandhomes-search/' + zipcode + '/beds-1/baths-1/type-single-family-home'
        session = requests.Session()
        headers = {'User-Agent': generate_user_agent()}

#        proxies = get_proxies()
#        proxy_pool = cycle(proxies)
#        proxy = next(proxy_pool)
        proxy = '110.232.80.234:4145'
#        try: 
        homepage = session.get(url, timeout = 15, verify='Lam_certificate_Realtor_June2019_2.cer', headers = headers, proxies={"http": proxy, "https": proxy}) # Mac
#            print(homepage)
#        except:
#                Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work. 
#                We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url 
#            print("Skipping. Connection error")
#        
#        homepage = session.get(url, timeout = 15, headers = headers, proxies={"http": proxy, "https": proxy}) # Mac
#        homepage = session.get(url, verify='Lam_certificate_Realtor_June2019.cer', timeout = 5, headers = headers) # PC
        tree = html.fromstring(homepage.content)
#        soup = BeautifulSoup(homepage.content, "html.parser")
        
        # update status
        print('Scraping data for zipcode (%s/%s): ' % (counter,len(zipcodes)) + str(zipcode))
        
        # find number of results returned
        resultcount_temp = tree.xpath('//span[@id="search-result-count"]//text()')
        if resultcount_temp:
            resultcount = int(re.findall(r'\s+(\d+)', resultcount_temp[0])[0])
            print('Getting %s results for zipcode %s' % (resultcount, zipcode))
        else:
            print('No results found for zipcode %s' % zipcode)
            continue

        # get listing and order of appearance ids
        listing_ids = list(OrderedDict.fromkeys(tree.xpath('//li[@class="component_property-card js-component_property-card js-quick-view"]//@data-propertyid')))
        order_ids = list(OrderedDict.fromkeys(tree.xpath('//div[@class="data-wrap"]//@id')))
        listing_order = dict(zip(listing_ids, order_ids))
        
        # create empty dataframe to catch listings within a zipcode
        data_zipcode = pd.DataFrame()
        
        # check zips for listing ids, only scrape those matching query zip
        for listing_id in listing_ids:
            order = listing_order[listing_id]
            xpath_zip = '//*[@id="' + listing_id + '"]//span[@class="listing-postal"]//text()' 
            listing_zip = tree.xpath(xpath_zip)
            if listing_zip[0] != zipcode:
                continue

            # scrape desired information for each listing using appropriate xpath
            address_raw = tree.xpath('//*[@id="' + listing_id + '"]//span[@class="listing-street-address"]//text()')
            city = tree.xpath('//*[@id="' + listing_id + '"]//span[@class="listing-city"]//text()')     
            state = tree.xpath('//*[@id="' + listing_id + '"]//span[@class="listing-region"]//text()') 
            zip_code = tree.xpath('//*[@id="' + listing_id + '"]//span[@class="listing-postal"]//text()') 
            price_raw = tree.xpath('//*[@id="' + listing_id + '"]//span[@class="data-price"]//text()') 
            beds_raw = tree.xpath('//*[@id="' + listing_id + '"]//span[@class="data-value meta-beds"]//text()') 
            baths_raw = tree.xpath('//*[@id="' + listing_id + '"]//li[@data-label="property-meta-baths"]//span[@class="data-value"]//text()') 
            homesize_raw = tree.xpath('//*[@id="' + listing_id + '"]//li[@data-label="property-meta-sqft"]//span[@class="data-value"]//text()')
            lotsize_raw = tree.xpath('//*[@id="' + listing_id + '"]//li[@data-label="property-meta-lotsize"]//text()')
            latitude = tree.xpath('//*[@id="' + order + '"]/div[1]/span[2]/meta[1]//@content')
            longitude = tree.xpath('//*[@id="' + order + '"]/div[1]/span[2]/meta[2]//@content')
            
            # if lot units are acres, change to sqft
            if len(lotsize_raw) == 2:
                if lotsize_raw[1] == ' acres':
                    lotsize = acretosqft(lotsize_raw[0])
                else:
                    lotsize = [lotsize_raw[0]]
            else:
                lotsize = lotsize_raw
            
            # create data frame from scraped data before cleaning
#            try:
            data_listing_temp = {'Address': flatten(address_raw), 'City': flatten(city),
                                 'State': flatten(state), 'Zip': flatten(zip_code), 
                                 'Price': flatten(price_raw), 
                                 'Beds': flatten(beds_raw), 'Baths': flatten(baths_raw), 
                                 'Home size': flatten(homesize_raw), 'Lot size': flatten(lotsize),  
                                 'Latitude': flatten(latitude), 'Longitude': flatten(longitude)}
        
        # compile data across listings within single zipcode
            df_data_listing_temp = pd.DataFrame(data_listing_temp, index = [order])
            data_zipcode = data_zipcode.append(df_data_listing_temp)          
         
#            except:
#                print('Zipcode %s was skipped' % zipcode)

        # compile listings across zipcodes
        data_all = data_all.append(data_zipcode)
        
        # every 10 zipcodes, save new copy of .csv file
        if counter % 10 == 0:
            csv_name = 'data_to_zipcode_' + str(counter) + '.csv'
            data_all.to_csv(csv_name)
        else:
            pass
                        
    return data_all
        
        