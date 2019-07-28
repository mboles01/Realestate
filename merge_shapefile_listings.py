#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:51:49 2019

@author: michaelboles
"""

import geopandas as gpd
shapefile_info = gpd.read_file(r'./shapefiles/Bay Zips/ZIPCODE.shp')
shapefile_info.to_csv('./data/data by zipcode/shapefile_data.csv')

# get full data set
import pandas as pd
data_all = pd.read_csv('./data/listings/data_all.csv')

# get zip codes from shapefile
shapefile_info.columns
shapefile_selected = shapefile_info[['ZIP_CODE_5', 'AREA', 'POPULATION', 'geometry']]
shapefile_selected = shapefile_selected.rename(index = str, 
                                               columns = {'ZIP_CODE_5': 'Zip', 
                                                          'POPULATION': 'Population', 
                                                          'AREA': 'Area'})
shapefile_zips = pd.DataFrame(shapefile_selected[['Zip', 'Population', 'Area']]).astype(int)

# get zip codes, commute time from full data set
data_selected_temp1 = data_all[['Zip','Min commute','School score']]
data_selected_temp2 = data_selected_temp1.groupby('Zip', as_index = False).mean()#.drop(columns = 'Grade') 

# round school score column
data_selected = data_selected_temp2.round({'School score': 1})

# get zip codes that are present in both shape file and main data set
data_zipcodes = shapefile_zips.merge(data_selected, on='Zip', how='left')

# save commute time to .csv
data_zipcodes.to_csv('./data/data by zipcode/data_zipcodes.csv')
