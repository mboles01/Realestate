# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:31:27 2019

@author: BolesMi
"""

# DEFINE DATA CLEANING FUNCTIONS 
import re

# from full address, pull out street address, city, and zipcode 
def address_clean(address_raw):
    address = []; city = []; zip_code = []
    for counter, line in enumerate(address_raw):
        address_temp2 = []; city_temp2 = []; zip_code_temp = []
        # get address
        try:
            address_temp = re.findall(r'\"(\S+\s\S+),|\"(\S+\s\S+\s\S+),|\"(\S+\s\S+\s\S+\s\S+),|\"(\S+\s\S+\s\S+\s\S+\s\S+),|\"(\S+\s\S+\s\S+\s\S+\s\S+\s\S+),',f'"{line}"')
            address_temp2 = list(filter(None, [i for i in address_temp[0]]))[0]
        except: 
            print('Failed to capture address of %s' % line)
            continue
        # get city
        try:
            city_temp = re.findall(r',\s(\w+), CA|,\s(\w+\s\w+), CA|,\s(\w+\s\w+\s\w+), CA|,\s(–), CA', line)
            city_temp2 = list(filter(None, [i for i in city_temp[0]]))[0]
        except:
            print('Failed to capture city of %s' % line)
            continue
        # get zipcode
        zip_code_temp = re.findall(r'CA, (\d\d\d\d\d)', line)[0]
        # if address, city, and zip have been pulled successfully, create objects
        if address_temp2 and city_temp2 and zip_code_temp:
            address.append(address_temp2)
            city.append(city_temp2)
            zip_code.append(zip_code_temp)
        else:
            pass
    return address, city, zip_code


# find beds, remove hyphens
def beds_clean(beds_raw):
    beds_temp1 = list(map(lambda m: tuple(filter(bool, m)), re.findall(r'(\d+/+\d+)|(\d+)|(–)',str(beds_raw))))
    beds_temp2 = [i[0] for i in beds_temp1]
    beds = [0 if i == '–' else int(i) for i in beds_temp2]
    return beds    

# need to remove whitespace, extra text, and convert slashes from baths
def baths_clean(baths_raw):
    baths_temp1 = list(map(lambda m: tuple(filter(bool, m)), re.findall(r'(\d+/+\d+)|(\d+)|(–/\d+)|(–)',str(baths_raw))))
    baths_temp2 =  [i[0] for i in baths_temp1]
    baths_temp3 = [re.sub('/1','.5', i) for i in baths_temp2]
    baths_temp4 = []
    for i in baths_temp3:
        if i[-2:] == '/2':
            baths_temp4.append(str(int(i[0])+1))
        elif i[-2:] == '/3':
            baths_temp4.append(str(int(i[0])+1.5))
        elif i[-2:] == '/4':
            baths_temp4.append(str(int(i[0])+2))        
        elif i[-2:] == '/5':
            baths_temp4.append(str(int(i[0])+2.5))
        elif i[0] == '–':
            baths_temp4.append(0)
        else:
            baths_temp4.append(i)
    baths = list(map(float, baths_temp4))
    return baths

# pull out home size entries, replace hyphens
def homesize_clean(homesize_raw):
    homesize = []
    for _ in range(0,int(len(homesize_raw)/6)):
        index = _*6+2
        homesize_temp1 = homesize_raw[index]   
        homesize_temp2 = re.sub(',','',homesize_temp1)        
        try: 
            homesize.append(int(homesize_temp2))
        except:
            homesize.append('0')
    return homesize



def sqft2acre(lotinsqft):
    return round(lotinsqft/43560,3)

# find lot size, convert sqft values to acres
def lot_clean(lot_raw):
    lot_temp1 = list(map(lambda m: tuple(filter(bool, m)), re.findall(r'(\d+\,\d\d\d)|(\d+\.\d+)|(\d+)|(–)', str(lot_raw))))
    lot_temp2 = [i[0] for i in lot_temp1]
    lot_temp3 = [re.sub(',','',i) for i in lot_temp2]
    lot_temp4 = [0 if i == '–' else i for i in lot_temp3]
    lot_temp5 = [float(i) for i in lot_temp4]
    lot = []
    for i in lot_temp5:
        if i > 100:      # assume if lot size is > 100 units are sqft not acres
            lot.append(sqft2acre(i))
        else:
            lot.append(i)
    return lot   

# find year, replace hyphens
def yearbuilt_clean(yearbuilt_raw):
    yearbuilt = []
    for _ in range(0,int(len(yearbuilt_raw)/10)):
        index = _*10+6
        yearbuilt_temp = yearbuilt_raw[index]   
        try: 
            yearbuilt.append(int(yearbuilt_temp))
        except:
            yearbuilt.append(0)
    return yearbuilt

# find garage, replace hyphens
def garage_clean(garage_raw):
    garage = []
    for _ in range(0,int(len(garage_raw)/5)):
        index = _*5+1
        garage_temp = garage_raw[index]   
        try: 
            garage.append(int(garage_temp))
        except:
            garage.append(0)
    return garage

