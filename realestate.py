
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


# web scrape: from https://docs.python-guide.org/scenarios/scrape/

# import modules
from lxml import html
import requests

# specify webpage to scrape

url = 'https://www.mlslistings.com/Search/Result/299ae029-54cd-404d-bf6c-edab2dc896cc/1'
page = requests.get(url, verify=False)
tree = html.fromstring(page.content)

# scrape desired information
address_raw = list(map(str, tree.xpath('//a[@class="search-nav-link"]//text()')))
price_raw = list(map(str, tree.xpath('//span[@class="font-weight-bold listing-price d-block pull-left pr-25"]//text()')))
hometype_raw = list(map(str, tree.xpath('//div[@class="listing-info clearfix font-size-sm line-height-base listing-type mb-25"]//text()')))
beds_raw = list(map(str, tree.xpath('//span[@class="listing-info-item font-size-sm line-height-base d-block pull-left pr-50 listing-beds"]//text()')))
baths_raw = list(map(str, tree.xpath('//span[@class="listing-info-item font-size-sm line-height-base d-block pull-left pr-50 listing-baths"]//text()')))
lot_raw = list(map(str, tree.xpath('//span[@class="listing-info-item font-size-sm line-height-base d-block pull-left pr-50 listing-lot-size"]//text()')))
garage_raw = list(map(str, tree.xpath('//span[@class="listing-info-item font-size-sm line-height-base d-block pull-left pr-50 listing-garage"]//text()')))
yearbuilt_raw = list(map(str, tree.xpath('//span[@class="listing-info-item font-size-sm line-height-base d-block pull-left pr-50 listing-sqft last"]//text()')))


# clean data
import re

# scraped address needs work: pull out address, city, zip separately...
address = list(map(str, re.findall(r'(.+),.+,.+,.+',str(address_raw))))

# convert price to integer
price = list(map(int, [re.sub('[$,]','',i) for i in price_raw]))

# need to remove extra whitespace from scraped hometype, beds, year, garage
hometype = re.findall(r'\s\s(\w+)',str(hometype_raw))
beds = list(map(int, re.findall(r'(\d+)',str(beds_raw))))
yearbuilt = list(map(int, re.findall(r'(\d\d\d\d)',str(yearbuilt_raw))))
garage = list(map(int, re.findall(r'(\d)',str(garage_raw))))

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

baths = baths_clean(baths_raw)

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
    
lot = lot_clean(lot_raw)

import pandas as pd

data = {'Address': address, 'Beds': beds, 'Baths': baths,
        'Lot size': lot, 'Year built': yearbuilt, 'Garage': garage, 
        'Home type': hometype, 'Price': price}

dataframe = pd.DataFrame(data)


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
