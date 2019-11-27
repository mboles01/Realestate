#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 16:43:36 2019

@author: michaelboles
"""

# set up working directory
import os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate/Data/ABB') # Mac

# import standard packages
import pandas as pd

# import custom histogram plotter
import sys
sys.path.append('./Scripts')
from plotfunctions import plothist, texthist, plothist_categorical

# import cleaned SF listing dataset
listings_sf_clean = pd.read_csv('./Data/Clean/San_Francisco/listings_sf_data_clean.csv')


### PLOT HISTOGRAMS - NUMERICAL ###

# revenue estimates

histogram_text = texthist(data = listings_sf_clean['monthly_revenue'], 
                          divide_median=1, divide_stdev=1, rounding=0,
                          decimals = 0, units = '', dollars = True)

name = './Images/monthly_revenue.jpg'
plothist(data = listings_sf_clean['monthly_revenue'], nbins = 35, nxticks = 6, roundx = 3, 
         textbox = histogram_text, text_xpos = .94, xmin = 0, xmax = 20000, shift = None,
         xlabel = 'Revenue per month ($)', ylabel = 'Counts', figure_name = name)



# prices

histogram_text = texthist(data = listings_sf_clean['price'], 
                          divide_median=1, divide_stdev=1, rounding=0,
                          decimals = 0, units = '', dollars = True)

name = './Images/prices.jpg'
plothist(data = listings_sf_clean['price'], nbins = 35, nxticks = 6, roundx = 2, 
         textbox = histogram_text, text_xpos = 0.94, xmin = 0, xmax = 800, shift = None,
         xlabel = 'Nightly price ($)', ylabel = 'Counts', figure_name = name)



# number of reviews

histogram_text = texthist(data = listings_sf_clean['number_of_reviews'], 
                          divide_median=1, divide_stdev=1, rounding=0,
                          decimals = 0, units = '', dollars = False)

name = './Images/number_of_reviews.jpg'
plothist(data = listings_sf_clean['number_of_reviews'], nbins = 35, nxticks = 5, roundx = 2, 
         textbox = histogram_text, text_xpos = 0.94, xmin = 0, xmax = 400, shift = None,
         xlabel = 'Number of reviews', ylabel = 'Counts', figure_name = name)



# number of reviews per month

histogram_text = texthist(data = listings_sf_clean['reviews_per_month'], 
                          divide_median=1, divide_stdev=1, rounding = 2,
                          decimals = 2, units = '', dollars = False)

name = './Images/reviews_per_month.jpg'
plothist(data = listings_sf_clean['number_of_reviews'], nbins = 35, nxticks = 5, roundx = 0, 
         textbox = histogram_text, text_xpos = 0.94, xmin = 0, xmax = 10, shift = None,
         xlabel = 'Reviews per month', ylabel = 'Counts', figure_name = name)



# number of reviews per month

histogram_text = texthist(data = listings_sf_clean['reviews_per_month'], 
                          divide_median=1, divide_stdev=1, rounding = 2,
                          decimals = 2, units = '', dollars = False)

name = './Images/reviews_per_month.jpg'
plothist(data = listings_sf_clean['number_of_reviews'], nbins = 35, nxticks = 5, roundx = 0, 
         textbox = histogram_text, text_xpos = 0.94, xmin = 0, xmax = 10, shift = None,
         xlabel = 'Reviews per month', ylabel = 'Counts', figure_name = name)



# cleaning fee

histogram_text = texthist(data = listings_sf_clean['cleaning_fee'], 
                          divide_median=1, divide_stdev=1, rounding = 0,
                          decimals = 0, units = '', dollars = False)

name = './Images/cleaning_fee.jpg'
plothist(data = listings_sf_clean['cleaning_fee'], nbins = 35, nxticks = 5, roundx = 1, 
         textbox = histogram_text, text_xpos = 0.94, xmin = 0, xmax = 300, shift = None,
         xlabel = 'Cleaning fee', ylabel = 'Counts', figure_name = name)


# availability 365

histogram_text = texthist(data = listings_sf_clean['availability_365'], 
                          divide_median=1, divide_stdev=1, rounding = 0,
                          decimals = 0, units = '', dollars = False)

name = './Images/availability_365.jpg'
plothist(data = listings_sf_clean['availability_365'], nbins = 35, nxticks = 5, roundx = 1, 
         textbox = histogram_text, text_xpos = 0.94, xmin = 0, xmax = 365, shift = None,
         xlabel = 'Availability (nights per year)', ylabel = 'Counts', figure_name = name)



# extra people

histogram_text = texthist(data = listings_sf_clean['extra_people'], 
                          divide_median=1, divide_stdev=1, rounding = 0,
                          decimals = 0, units = '', dollars = False)

name = './Images/extra_people.jpg'
plothist(data = listings_sf_clean['extra_people'], nbins = 35, nxticks = 5, roundx = 1, 
         textbox = histogram_text, text_xpos = 0.94, xmin = 0, xmax = 120, shift = None,
         xlabel = 'Extra person charge ($)', ylabel = 'Counts', figure_name = name)



# bedrooms 

histogram_text = texthist(data = listings_sf_clean['bedrooms'], 
                          divide_median=1, divide_stdev=1, rounding = 0,
                          decimals = 0, units = '', dollars = False)

name = './Images/bedrooms.jpg'
plothist(data = listings_sf_clean['bedrooms'], nbins = 5, nxticks = 5, roundx = 0, 
         textbox = histogram_text, text_xpos = 0.94, xmin = 0, xmax = 5, shift = 0.5,
         xlabel = 'Number of bedrooms', ylabel = 'Counts', figure_name = name)


### PLOT HISTOGRAMS - CATEGORICAL ###

# property type

name = './Images/property_type.jpg'

plothist_categorical(data = listings_sf_clean['property_type'], ncategories = 7, 
                     title = 'Property type', rotation = 45, figure_name = name,
                     xdim = 7, ydim = 7)

# room type

name = './Images/room_type.jpg'

plothist_categorical(data = listings_sf_clean['room_type'], ncategories = 4, 
                     title = 'Room type', rotation = 45, figure_name = name,
                     xdim = 4, ydim = 7)

# neighborhood

name = './Images/neighbourhood.jpg'

plothist_categorical(data = listings_sf_clean['neighbourhood'], ncategories = 25, 
                     title = 'Neighborhood', rotation = 45, figure_name = name,
                     xdim = 20, ydim = 7)


# host name

name = './Images/host_name.jpg'

plothist_categorical(data = listings_sf_clean['host_name'], ncategories = 25, 
                     title = 'Host name', rotation = 45, figure_name = name,
                     xdim = 20, ydim = 7)

