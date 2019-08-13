#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 14:03:32 2019

@author: michaelboles
"""

# import modules
from bs4 import BeautifulSoup
from lxml import html
import requests
import pandas as pd
import time
from user_agent import generate_user_agent


# get homepage session
zipcode = 95126
url = 'https://www.ziprealty.com/schools/California/' + str(zipcode)
url = 'https://www.greatschools.org/search/search.page?distance=2&lat=37.3290122&locationLabel=San%20Jose%2C%20CA%2095126&locationType=zip&lon=-121.91602109999997&sort=distance&st=public_charter&st=public&st=charter&state=CA'
session = requests.Session()
headers = {'User-Agent': generate_user_agent()}

homepage = session.get(url, timeout = 15, headers = headers)
tree = html.fromstring(homepage.content)

#shows very small soup file - doesn't match html in browser - why?
soup = BeautifulSoup(homepage.content, "html.parser")

# get data - doesn't work because homepage.content is no good
tree.xpath('//span[@class="icoSchoolScore bgcolor-yellow"]//text()')


<div class="circle-rating--small circle-rating--3">3<span
tree.xpath('//div[@class="circle-rating--small circle-rating--3"]//@content')
           
tree.xpath('//div[@class="l-fixed"]//@content')
tree.xpath('//span[@class="sr-only"]//@content')

tree.xpath('//a[@class="search-nav-link"]//text()'