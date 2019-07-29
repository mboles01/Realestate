#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 14:14:07 2019

@author: michaelboles
"""

# import packages
import numpy as np
import matplotlib.pyplot as plt

# plot histogram

def plothist(data, binwidth, textbox, xmin, xmax, xlabel, ylabel, figure_name):
    fig, ax = plt.subplots(1,1,figsize=(7,7))
    bins = np.arange(round(min(data),1), max(data) + binwidth, binwidth)
    props = dict(facecolor='white', alpha=1.0)

    ax.hist(data, bins, edgecolor = 'black', facecolor = 'blue')
    
    plt.xlim(xmin, xmax); plt.xlabel(xlabel, fontsize = 18, fontname = 'Helvetica')
    plt.ylabel(ylabel, fontsize = 18)
    ax.tick_params(axis = 'x', labelsize = 14); ax.tick_params(axis = 'y', labelsize = 14)
    ax.text(0.575, 0.97, textbox, transform = ax.transAxes, fontsize = 18, fontname = 'Helvetica', verticalalignment = 'top', bbox = props)
    
    for tick in ax.get_xticklabels():
        tick.set_fontname('Helvetica')
    for tick in ax.get_yticklabels():
        tick.set_fontname('Helvetica')
    
    plt.rcParams['axes.unicode_minus'] = False
    plt.grid(); ax.set_axisbelow(True)
    plt.savefig(figure_name, dpi = 600)
    plt.show()


#def plothist2(data, binwidth, xmin, xmax, xlabel, ylabel):
#    fig, ax = plt.subplots(1,1,figsize=(7,7))
#    bins = np.arange(round(min(data),1), max(data) + binwidth, binwidth)
#
#    ax.hist(data, bins, edgecolor = 'black', facecolor = 'blue')
#    
#    plt.xlim(xmin, xmax); plt.xlabel(xlabel, fontsize = 18, fontname = 'Helvetica')
#    plt.ylabel(ylabel, fontsize = 18)
#    ax.tick_params(axis = 'x', labelsize = 14); ax.tick_params(axis = 'y', labelsize = 14)
#    
#    for tick in ax.get_xticklabels():
#        tick.set_fontname('Helvetica')
#    for tick in ax.get_yticklabels():
#        tick.set_fontname('Helvetica')
#    
#    plt.rcParams['axes.unicode_minus'] = False
#    plt.grid(); ax.set_axisbelow(True)
#    plt.show()
