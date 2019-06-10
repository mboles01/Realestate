
# set up working directory
import sys, os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate')

# import zipcodes
import csv

#filename='zipcodes.csv'
def csvread(filename):
    with open('zipcodes.csv', mode='r') as f:
        reader = csv.reader(f, delimiter=',')
        ziptable = [row for row in reader]
        zipcodes = [i[0] for i in ziptable][1:]
    f.close()
    return zipcodes

# define data cleaning functions

def address_clean(address_raw):
    address_temp = list(map(lambda m: tuple(filter(bool, m)), 
                   re.findall(r'(\d+\s\w+),|(\d+\s\w+\s\w+),|(\d+\s\w+\s\w+\s\w+),',str(address_raw))))
    address = [i[0] for i in address_temp]
    return address

def city_clean(address_raw):
    city_temp = list(map(lambda m: tuple(filter(bool, m)),re.findall(r',\s(\w+), CA|,\s(\w+\s\w+), CA',str(address_raw))))
    city = [i[0] for i in city_temp]
    return city

# need to remove whitespace, extra text, and convert slashes from baths
def baths_clean(baths_raw):
    baths_temp1 = list(map(lambda m: tuple(filter(bool, m)), re.findall(r'(\d+/+\d+)|(\d+)',str(baths_raw))))
    baths_temp2 =  [i[0] for i in baths_temp1]
    baths_temp3 = [re.sub('/1','.5', i) for i in baths_temp2]
    baths_temp4 = []
    for i in baths_temp3:
        if i[-2:] == '/2':
            baths_temp4.append(str(int(i[0])+1))
        else:
            baths_temp4.append(i)
    baths = list(map(float, baths_temp4))
    return baths


def sqft2acre(lotinsqft):
    return round(lotinsqft/43560,3)

# need to remove extra text, whitespace, and convert sqft values to acres
def lot_clean(lot_raw):
    lot_temp1 = list(map(lambda m: tuple(filter(bool, m)), re.findall(r'(\d\,\d\d\d)|(\d\.\d+)', str(lot_raw))))
    lot_temp2 = [i[0] for i in lot_temp1]
    lot_temp3 = [re.sub(',','',i) for i in lot_temp2]
    lot_temp4 = [float(i) for i in lot_temp3]
    lot = []
    for i in lot_temp4:
        if i > 10:      # assume if lot size is > 10 units are sqft not acres
            lot.append(sqft2acre(i))
        else:
            lot.append(i)
    return lot


# web scrape

# import modules
from bs4 import BeautifulSoup
from lxml import html
import requests
import pandas as pd
import time

# scrape MLS

zipcodes = ['94401']#,'94401']

# create empty data frame
data_all = pd.DataFrame()

for zipcode in zipcodes:
    
    # get homepage session
    session = requests.Session()
    homepage = session.get('https://www.mlslistings.com/')
    soup = BeautifulSoup(homepage.content, "html.parser")
    
    # get security token, post search data
    token = soup.find("input", attrs={"name" : "__RequestVerificationToken"})['value']
    data = {'transactionType': 'buy', 'listing_status': 'Active', 'searchTextType': '', 'searchText': zipcode,'__RequestVerificationToken': token, 'property_type': 'SingleFamilyResidence'}
    search_results = session.post("https://www.mlslistings.com/Search/ResultPost", data=data)
    tree = html.fromstring(search_results.content)
    
    # scrape desired information
    address_raw = list(map(str, tree.xpath('//a[@class="search-nav-link"]//text()')))
    price_raw = list(map(str, tree.xpath('//span[@class="font-weight-bold listing-price d-block pull-left pr-25"]//text()')))
    hometype_raw = list(map(str, tree.xpath('//div[@class="listing-info clearfix font-size-sm line-height-base listing-type mb-25"]//text()')))
    beds_raw = list(map(str, tree.xpath('//span[@class="listing-info-item font-size-sm line-height-base d-block pull-left pr-50 listing-beds"]//text()')))
    baths_raw = list(map(str, tree.xpath('//span[@class="listing-info-item font-size-sm line-height-base d-block pull-left pr-50 listing-baths"]//text()')))
    lot_raw = list(map(str, tree.xpath('//span[@class="listing-info-item font-size-sm line-height-base d-block pull-left pr-50 listing-lot-size"]//text()')))
    garage_raw = list(map(str, tree.xpath('//span[@class="listing-info-item font-size-sm line-height-base d-block pull-left pr-50 listing-garage"]//text()')))
    yearbuilt_raw = list(map(str, tree.xpath('//span[@class="listing-info-item font-size-sm line-height-base d-block pull-left pr-50 listing-sqft last"]//text()')))

    # update status

    # clean raw data
    import re
    address = address_clean(address_raw)
    city = city_clean(address_raw)
    zip_code = re.findall(r'\d\d\d\d\d',str(address_raw))
    beds = list(map(int, re.findall(r'(\d+)',str(beds_raw))))
    baths = baths_clean(baths_raw)
    lot = lot_clean(lot_raw)
    yearbuilt = list(map(int, re.findall(r'(\d\d\d\d)',str(yearbuilt_raw))))
    garage = list(map(int, re.findall(r'(\d)',str(garage_raw))))
    hometype = re.findall(r'\s\s(\w+\s\w+\s\w+)',str(hometype_raw))
    price = list(map(int, [re.sub('[$,]','',i) for i in price_raw]))
    
    # create data frame from scraped, cleaned data
    data_temp = {'Address': address, 'City': city, 'Zip': zip_code, 'Beds': beds, 'Baths': baths,
        'Lot size': lot, 'Year built': yearbuilt, 'Garage': garage, 
        'Home type': hometype, 'Price': price}
    dataframe_temp = pd.DataFrame(data_temp)
    data_all = data_all.append(dataframe_temp)
    
    # wait 2 seconds, then scrape next zipcode
    time.sleep(2)


# Calls the above functions
def main():
    if len(sys.argv) != 2:
        print('usage: python realestate.py zipcodes')
        sys.exit(1)
    zips = csvread(sys.argv[1])
    print(zips)

# Calls the main function
if __name__ == '__main__':
  main()
