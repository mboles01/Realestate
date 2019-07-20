# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:31:23 2019

@author: michaelboles
"""

# set up working directory
import os
#os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import master dataset    
data_bay_withtimes = pd.read_csv('./data/data_bay_withtimes.csv')

# import ancillary dataset
data_schools = pd.read_csv('./School data/school_quality_bay.csv')

# merge school quality with master dataset
data_all_temp1 = data_bay_withtimes.merge(data_schools, on='Zip', how='left')

# add shorter commute time column
data_all_temp1['Min commute'] = data_all_temp1[['SF time', 'PA time']].min(axis=1)

# remove spaces in column names - necessary for OLS?
data_all_temp1.columns = data_all_temp1.columns.str.replace(' ', '_')

# format/clean -- select columns of interest, drop rows with zeros, NaNs
data_all_temp2 = data_all_temp1[['Zip', 'Beds', 'Baths', 'Home_size', 'Lot_size', 'Min_commute', 'School_score', 'Price']] #'SF_time', 'PA_time'
data_all_temp3 = data_all_temp2.dropna()
data_all_temp4 = data_all_temp3[(data_all_temp3 != 0).all(1)]

# get rid of some outliers
data_all_temp5 = data_all_temp4[data_all_temp4['Home_size'] < 5000]
data_all_temp6 = data_all_temp5[data_all_temp5['Lot_size'] < 20000]
data_all_temp7 = data_all_temp6[data_all_temp6['Price'] < 4000000]
data_all_temp8 = data_all_temp7[data_all_temp7['Beds'] < 6]
data_all_temp9 = data_all_temp8[data_all_temp8['Baths'] <= 5]

# rescale for pairplot
data_all_temp9['Price'] = data_all_temp9['Price']/1000000

# rename series for pairplot
data_all = data_all_temp9.rename(columns = {'Home_size': 'Home size (sqft)', 
                                            'Lot_size': 'Lot size (sqft)',
                                            'Min_commute': 'Commute time (mins)',
                                            'School_score': 'School score (%)',
                                            'Price': 'Price ($M)'})

# get correlations, round
corr_beds_price = round(data_all['Beds'].corr(data_all['Price ($M)']),2)
corr_baths_price = round(data_all['Baths'].corr(data_all['Price ($M)']),2)
corr_home_price = round(data_all['Home size (sqft)'].corr(data_all['Price ($M)']),2)
corr_lot_price = round(data_all['Lot size (sqft)'].corr(data_all['Price ($M)']),2)
corr_commute_price = round(data_all['Commute time (mins)'].corr(data_all['Price ($M)']),2)
corr_school_price = round(data_all['School score (%)'].corr(data_all['Price ($M)']),2)


# create pairplot with only price as y-axis

# home-only data
sns.set(style="ticks", color_codes=True)
g = sns.pairplot(data_all, 
             plot_kws=dict(line_kws=dict(color = '#3148a3'), 
                           scatter_kws=dict(facecolor = '#5797ff', edgecolor = '#3148a3', 
                                            linewidth = 0.33, alpha = 0.1, s = 20)),
             x_vars = ['Beds', 'Baths', 'Home size (sqft)', 'Lot size (sqft)'], 
             y_vars = 'Price ($M)', kind = 'reg')
spacing = 0.235
g.fig.text(0.08, 0.825, r'$R^{2}$ = ' + str(corr_beds_price), fontsize=10)
g.fig.text(0.08 + spacing, 0.825, r'$R^{2}$ = ' + str(corr_baths_price), fontsize=10)
g.fig.text(0.08 + 2*spacing, 0.825, r'$R^{2}$ = ' + str(corr_home_price), fontsize=10)
g.fig.text(0.08 + 3*spacing, 0.825, r'$R^{2}$ = ' + '0.30', fontsize=10)

g.savefig('pairplot_price_home.jpg', dpi=600)

# home + surroundings data
g = sns.pairplot(data_all, 
             plot_kws=dict(line_kws=dict(color = '#3148a3'), 
                           scatter_kws=dict(facecolor = '#5797ff', edgecolor = '#3148a3', 
                                            linewidth = 0.33, alpha = 0.1, s = 20)),
             x_vars = ['Beds', 'Baths', 'Home size (sqft)', 'Lot size (sqft)', 
                      'Commute time (mins)', 'School score (%)'], 
             y_vars = 'Price ($M)', kind = 'reg')
spacing2 = (4/6)*spacing + 0.0025
g.fig.text(0.06, 0.825, r'$R^{2}$ = ' + str(corr_beds_price), fontsize=10)
g.fig.text(0.06 + spacing2, 0.825, r'$R^{2}$ = ' + str(corr_baths_price), fontsize=10)
g.fig.text(0.06 + 2*spacing2, 0.825, r'$R^{2}$ = ' + str(corr_home_price), fontsize=10)
g.fig.text(0.06 + 3*spacing2, 0.825, r'$R^{2}$ = ' + '0.30', fontsize=10)
g.fig.text(0.06 + 4*spacing2, 0.825, r'$R^{2}$ = ' + str(corr_commute_price), fontsize=10)
g.fig.text(0.06 + 5*spacing2, 0.825, r'$R^{2}$ = ' + str(corr_school_price), fontsize=10)

g.savefig('pairplot_price_all.jpg', dpi=600)

# create overall pairplot

def corrfunc(x, y, **kws):
    r = x.corr(y)
    ax = plt.gca()
    ax.annotate(r'$R^{2}$ = ' + str(round(r, 2)), xy=(.1, .9), xycoords=ax.transAxes, backgroundcolor = 'white')

g = sns.pairplot(data_all, diag_kind = 'kde', kind = 'reg',
             plot_kws=dict(line_kws=dict(color = '#3148a3'), 
                           scatter_kws=dict(facecolor = '#5797ff', edgecolor = '#3148a3', 
                                            linewidth = 0.33, alpha = 0.1, s = 20)),
             x_vars = ['Beds', 'Baths', 'Home size (sqft)', 'Lot size (sqft)', 
                      'Commute time (mins)', 'School score (%)'], 
             y_vars = ['Beds', 'Baths', 'Home size (sqft)', 'Lot size (sqft)', 
                       'Commute time (mins)', 'School score (%)'])
g.map_lower(corrfunc)
g.savefig('pairplot_data_all_price.jpg', dpi=300)



# count number, frequency of unique zipcodes
cityzips = data_bay_withtimes[['City','Zip']]
numzips = data_bay_withtimes['Zip'].nunique()
topzips = data_bay_withtimes['Zip'].value_counts().to_frame()
topzips['Count'] = topzips['Zip']
topzips['Zip'] = topzips.index
topzips_city = topzips.merge(cityzips, on='Zip', how='inner')

# option to select one zipcode
zipcode = 95126
data_subset = data_all[data_all['Zip'] == zipcode]

## or zipcode range
#lozip = 95029; hizip = 95031
#data_subset_temp1 = data_temp3[(data_temp3['Zip'] > lozip) & (data_temp3['Zip'] < hizip)]

## option to remove outliers
#z = np.abs(stats.zscore(data_temp4[['Beds', 'Baths', 'Home_size', 'Lot_size', 
#                                  'SF_time', 'PA_time', 'Min_commute', 'Price']]))
#data_to_fit = data_temp4[(z < 3).all(axis=1)]
##data_to_fit = data_temp4

# get correlations within data subset
corr_beds_price_subset = round(data_subset['Beds'].corr(data_subset['Price ($M)']),2)
corr_baths_price_subset = round(data_subset['Baths'].corr(data_subset['Price ($M)']),2)
corr_home_price_subset = round(data_subset['Home size (sqft)'].corr(data_subset['Price ($M)']),2)
corr_lot_price_subset = round(data_subset['Lot size (sqft)'].corr(data_subset['Price ($M)']),2)


## create subset pairplot
#sns.set(style="ticks", color_codes=True)
#sns.pairplot(data_subset.drop('Zip', axis = 1), diag_kind = 'kde', kind = 'reg',
#             plot_kws = dict(scatter_kws = dict(edgecolor = 'w')))

# create pairplot with only price as y-axis
sns.set(style="ticks", color_codes=True)
g = sns.pairplot(data_subset, 
             plot_kws=dict(line_kws=dict(color = '#3148a3'), 
                           scatter_kws=dict(facecolor = '#5797ff', edgecolor = '#3148a3', 
                                            linewidth = 0.33, alpha = 1, s = 20)),
             x_vars = ['Beds', 'Baths', 'Home size (sqft)', 'Lot size (sqft)'], 
             y_vars = 'Price ($M)', kind = 'reg')
spacing = 0.235
g.fig.text(0.08, 0.825, r'$R^{2}$ = ' + str(corr_beds_price_subset), fontsize=10)
g.fig.text(0.08 + spacing, 0.825, r'$R^{2}$ = ' + str(corr_baths_price_subset), fontsize=10)
g.fig.text(0.08 + 2*spacing, 0.825, r'$R^{2}$ = ' + '0.90', fontsize=10)
g.fig.text(0.08 + 3*spacing, 0.825, r'$R^{2}$ = ' + str(corr_lot_price_subset), fontsize=10)

g.savefig('pairplot_price_subset_' + str(zipcode) + '.jpg', dpi=900)

