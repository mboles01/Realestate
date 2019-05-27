#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 10:03:23 2019

@author: michaelboles
"""

# set up working directory
import os
os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac

# import master dataset    
import pandas as pd
data_all = pd.read_csv('data_all.csv')

# import packages
import numpy as np
import matplotlib.pyplot as plt

# price analysis
prices_raw = data_all['Price']
prices = prices_raw/1000000

mean = round(np.average(prices))
median = np.median(prices)
stdev = np.std(prices)

# set up text box
textbox = 'Average = $%.2f M \nMedian = $%.2f M \nStdev = $%.2f M' % (mean, median, stdev)
props = dict(facecolor='white', alpha=1.0)

# set up histogram
binwidth = 0.1
bins=np.arange(round(min(prices),1), max(prices) + binwidth, binwidth)

# plot prices
fig, ax = plt.subplots(1,1,figsize=(7,7))
ax.hist(prices, bins, edgecolor = 'black', facecolor = 'blue')
plt.xlim(0,5); plt.xlabel('Price ($M)', fontsize = 18, fontname = 'Arial')
plt.ylabel('Counts', fontsize = 18)
ax.tick_params(axis = 'x', labelsize = 14); ax.tick_params(axis = 'y', labelsize = 14)
ax.text(0.565, 0.97, textbox, transform = ax.transAxes, fontsize = 18, fontname = 'Arial', verticalalignment = 'top', bbox = props)
for tick in ax.get_xticklabels():
    tick.set_fontname('Arial')
for tick in ax.get_yticklabels():
    tick.set_fontname('Arial')

plt.grid(); ax.set_axisbelow(True)
plt.show()




####


binwidth = 1
hist = np.histogram(edge_nm_norm[:,1], bins=np.arange(min(edge_nm_norm[:,1]), max(edge_nm_norm[:,1]) + binwidth, binwidth))
max_y = max(hist[0])


# plot image with extracted edge, plot histogram
from matplotlib_scalebar.scalebar import ScaleBar
scalebar = ScaleBar(calib, location = 'lower left')
caption = str('Image: ') + str(myimage) + str('   Top: ') + str(topcrop) + str('  Bot: ') + str(botcrop) + str('  Poly: ') + str(poly_order)

fig, (ax1,ax2) = plt.subplots(1,2,figsize=(14.5,4), gridspec_kw = {'width_ratios':[4, 1.25]})

ax1.imshow(im1[0:pic_bottom,:],cmap = 'gray')
ax1.scatter(edge_nocrop[:,0], edge_nocrop[:,1], s=.05, c='b')
ax1.add_artist(scalebar)
plt.xlim(0,im1.shape[1])
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
props = dict(boxstyle='none', facecolor='none', alpha=0.5)
ax1.text(0.25, -0.05, caption, transform=ax1.transAxes, fontsize=12, verticalalignment='top')

binwidth = 1
ax2.hist(edge_nm_norm[:,1], bins=np.arange(min(edge_nm_norm[:,1]), max(edge_nm_norm[:,1]) + binwidth, binwidth), color = 'b', edgecolor = 'k')
plt.xlim(-15,15); plt.xticks(np.arange(-15, 16, 5))
plt.ylim(0,1.15*max_y)
props = dict(boxstyle='square', facecolor='gray', alpha=0.5)
ax2.set_xlabel('Recess depth - mean recess depth (nm)'), ax2.set_ylabel('Counts')
ax2.text(1.125, .965, textbox, transform=ax1.transAxes, fontsize=12, verticalalignment='top', bbox=props)
plt.tight_layout()





width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
ax = plt.bar(center, hist, align='center', width=width)
plt.xlim(0,10000000)

textstr = '\n'.join((
    r'$\mu=%.2f$' % (mean, ),
    r'$\mathrm{median}=%.2f$' % (median, ),
    r'$\sigma=%.2f$' % (stdev, )))

#ax.hist(x, 50)
# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# place a text box in upper left in axes coords
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)

plt.show()



