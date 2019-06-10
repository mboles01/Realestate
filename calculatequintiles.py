#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 15:14:48 2019

@author: michaelboles
"""

# calculate quintiles of price distribution
import numpy as np
def price_quintiles(data):
    p20_price = np.percentile(data.loc[:,"Price"], 20) # return 20th percentile
    p40_price = np.percentile(data.loc[:,"Price"], 40) # return 40th percentile
    p60_price = np.percentile(data.loc[:,"Price"], 60) # return 60th percentile
    p80_price = np.percentile(data.loc[:,"Price"], 80) # return 80th percentile
    pricequintiles = [p20_price, p40_price, p60_price, p80_price]
    return pricequintiles

# calculate quintiles of price per sqft distribution
def pricepersqft_quintiles(data):
    p20_pricepersqft = np.percentile(data.loc[:,"Price per sqft"], 20) # return 20th percentile
    p40_pricepersqft = np.percentile(data.loc[:,"Price per sqft"], 40) # return 40th percentile
    p60_pricepersqft = np.percentile(data.loc[:,"Price per sqft"], 60) # return 60th percentile
    p80_pricepersqft = np.percentile(data.loc[:,"Price per sqft"], 80) # return 80th percentile
    pricepersqftquintiles = [p20_pricepersqft, p40_pricepersqft, p60_pricepersqft, p80_pricepersqft]
    return pricepersqftquintiles

# calculate quintiles of price per lot sqft distribution
def priceperlotsqft_quintiles(data):
    p20_priceperlotsqft = np.percentile(data.loc[:,"Price per lot sqft"], 20) # return 20th percentile
    p40_priceperlotsqft = np.percentile(data.loc[:,"Price per lot sqft"], 40) # return 40th percentile
    p60_priceperlotsqft = np.percentile(data.loc[:,"Price per lot sqft"], 60) # return 60th percentile
    p80_priceperlotsqft = np.percentile(data.loc[:,"Price per lot sqft"], 80) # return 80th percentile
    priceperlotsqftquintiles = [p20_priceperlotsqft, p40_priceperlotsqft, p60_priceperlotsqft, p80_priceperlotsqft]
    return priceperlotsqftquintiles
