
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

url = 'https://www.mlslistings.com/Search/Result/5d7bfc3d-5380-4f74-beda-b4a787e3a1f3/1'
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
hometype = re.findall(r'\s\s(\w+)',str(hometype_raw))
beds = re.findall(r'(\d+)',str(beds_raw))


baths_temp = list(map(lambda m: tuple(filter(bool, m)), re.findall(r'(\d+/+\d+)|(\d+)',str(baths_raw))))


baths_temp = re.findall(r'([\d+/])', str(baths_raw))  # need to fix
baths = []
for element in baths_temp:
    if baths_temp[element+1] == '/'
    baths = 



lot = re.findall(r'(\d\,\d\d\d)' | r'(\d\.\d\d)', str(lot_raw))
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
