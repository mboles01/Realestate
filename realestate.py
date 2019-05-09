
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
address = address_raw
price = price_raw

hometype = re.findall(r'\s\s(\w+)',str(hometype_raw))
beds = re.findall(r'(\d+)',str(beds_raw))

baths_temp1 = list(map(lambda m: tuple(filter(bool, m)), re.findall(r'(\d+/+\d+)|(\d+)',str(baths_raw))))
baths_temp2 =  [i[0] for i in baths_temp1]
baths = [re.sub('/1','.5', i) for i in baths_temp2]

def sqft2acre(match):
    match = match.group()
    return str(match/43560)

lot_temp1 = list(map(lambda m: tuple(filter(bool, m)), re.findall(r'(\d\,\d\d\d)|(\d\.\d+)', str(lot_raw))))
lot_temp2 = [i[0] for i in lot_temp1]
lot = [re.sub(r'\d\,\d\d\d', sqft2acre, i) for i in lot_temp2]  # need to fix -- -temp2 array prints vertically, diff from baths_temp2

yearbuilt = re.findall(r'(\d\d\d\d)',str(yearbuilt_raw))


junk = re.findall(r'(\\r\\n\s+)',str(baths_raw))



                            

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
