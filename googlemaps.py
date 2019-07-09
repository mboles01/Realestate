# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:07:06 2019

@author: BolesMi
"""

# set up working directory
import os
#os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import api key
with open('api.txt') as f:
    api_key = f.readline()
    f.close
    
    