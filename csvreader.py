# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:40:43 2019

@author: BolesMi
"""

# import zipcodes
import csv

#filename='zipcodes.csv'
def csvread(filename):
    with open(filename, mode='r') as f:
        reader = csv.reader(f, delimiter=',')
        ziptable = [row for row in reader]
        zipcodes_all = [i[0] for i in ziptable][1:]
    f.close()
    return zipcodes_all