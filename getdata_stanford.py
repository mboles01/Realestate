#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:51:49 2019

@author: michaelboles
"""

import geopandas as gpd
shapefile_info = gpd.read_file(r'./shapefiles/Bay Zips/ZIPCODE.shp')
shapefile_info.to_csv('./data/data by zipcode/shapefile_data.csv')


# get zip codes from shapefile
shapefile_info.columns
shapefile_selected = shapefile_info[['ZIP_CODE_5', 'AREA', 'POPULATION', 'geometry']]
shapefile_selected = shapefile_selected.rename(index = str, 
                                               columns = {'ZIP_CODE_5': 'Zip', 
                                                          'POPULATION': 'Population', 
                                                          'AREA': 'Area'})
shapefile_zips = pd.DataFrame(shapefile_selected[['Zip', 'Population', 'Area']]).astype(int)

# get zip codes, commute time from full data set
data_bay_ziptimes = data_bay_withtimes[['Zip','Min commute']]
data_bay_ziptimes2 = data_bay_ziptimes.groupby('Zip', as_index = False).mean()#.drop(columns = 'Grade')

# get zip codes that are present in both shape file and main data set
commute_time = shapefile_zips.merge(data_bay_ziptimes2, on='Zip', how='left')

# save commute time to .csv
commute_time.to_csv('./data/data by zipcode/commute_time.csv')