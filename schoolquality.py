# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:58:09 2019

@author: BolesMi
"""

# set up working directory
import os
#os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import packages
import pandas as pd

# import school grades dataset    
school_grades_raw = pd.read_csv('./School data/sb_ca2018_1_csv_v3.txt')

# keep school code, grade, standard met/above
school_grades_temp1 = school_grades_raw[['School Code', 'Grade', 'Percentage Standard Met and Above']].copy()

# rename school score column
school_grades_temp1 = school_grades_temp1.rename(index = str, columns = {'Percentage Standard Met and Above': 'Score'})

# remove values of * and 0
school_grades_temp2 = school_grades_temp1[school_grades_temp1['Score'].str.contains('\*')==False]
school_grades_temp2['Score'] = school_grades_temp2['Score'].astype('float64')
school_grades_temp3 = school_grades_temp2.loc[(school_grades_temp2!=0).all(axis=1)]

# collapse dataframe, displaying one (avg) grade per grade level
school_grades = school_grades_temp3.groupby('School Code', as_index = False).mean().drop(columns = 'Grade')

# bring in zipcodes
school_zipcodes_raw = pd.read_csv('./School data/sb_ca2018entities_csv.txt', encoding = 'latin_1')
school_zipcodes = school_zipcodes_raw[['Zip Code', 'School Code', 'School Name']].copy()

# merge data sets
school_quality_temp1 = school_grades.merge(school_zipcodes, on='School Code', how='inner')
school_quality_temp1['Zip Code'] = school_quality_temp1['Zip Code'].astype('int64')

# collapse dataframe, displaying one (avg) score per zip code
school_quality_temp2 = school_quality_temp1.groupby('Zip Code', as_index = False).mean().drop(columns = ['School Code'])

# filter only zip codes belonging to bay area
school_quality_bay = school_quality_temp2[(school_quality_temp2['Zip Code'] > 94000) & (school_quality_temp2['Zip Code'] < 96000)].reset_index(drop = True)

# write .csv file with data
school_quality_bay.to_csv('school_quality_bay.csv')
school_quality_temp1.to_csv('school_quality_all.csv')
