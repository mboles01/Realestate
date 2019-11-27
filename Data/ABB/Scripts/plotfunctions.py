#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 14:14:07 2019

@author: michaelboles
"""

# import packages
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


# set up histogram text box
def texthist(data, divide_median, divide_stdev, rounding, decimals, units, dollars):
    description = data.describe()
    
    if dollars == True:
        
        if decimals == 0:
            textbox = 'Median = $%.0f%s \nSt. dev. = $%.0f %s' % (round(description['50%']/divide_median, rounding), units, round(description['std']/divide_stdev,rounding), units) 
        elif decimals == 1:
            textbox = 'Median = $%.1f%s \nSt. dev. = $%.1f %s' % (round(description['50%']/divide_median, rounding), units, round(description['std']/divide_stdev,rounding), units) 
        elif decimals == 2:
            textbox = 'Median = $%.2f%s \nSt. dev. = $%.2f %s' % (round(description['50%']/divide_median, rounding), units, round(description['std']/divide_stdev,rounding), units) 
        elif decimals == 3:
            textbox = 'Median = $%.3f%s \nSt. dev. = $%.3f %s' % (round(description['50%']/divide_median, rounding), units, round(description['std']/divide_stdev,rounding), units) 
        
    elif dollars == False:
        
        if decimals == 0:
            textbox = 'Median = %.0f%s \nSt. dev. = %.0f %s' % (round(description['50%']/divide_median, rounding), units, round(description['std']/divide_stdev,rounding), units) 
        elif decimals == 1:
            textbox = 'Median = %.1f%s \nSt. dev. = %.1f %s' % (round(description['50%']/divide_median, rounding), units, round(description['std']/divide_stdev,rounding), units) 
        elif decimals == 2:
            textbox = 'Median = %.2f%s \nSt. dev. = %.2f %s' % (round(description['50%']/divide_median, rounding), units, round(description['std']/divide_stdev,rounding), units) 
        elif decimals == 3:
            textbox = 'Median = %.3f%s \nSt. dev. = %.3f %s' % (round(description['50%']/divide_median, rounding), units, round(description['std']/divide_stdev,rounding), units)  
    
    return textbox

# plot histograms

def plothist(data, nbins, nxticks, roundx, textbox, text_xpos, shift, 
             xmin, xmax, xlabel, ylabel, figure_name):
    
    fig, ax = plt.subplots(1,1,figsize=(7,7))
    binwidth = (xmax - xmin)/nbins
    bins = np.arange(round(min(data),1), max(data) + binwidth, binwidth)
    if shift != None:
        bins = bins + shift
    props = dict(facecolor='white', alpha=1.0, pad=10)

    ax.hist(data, bins, edgecolor = 'black', facecolor = 'blue')
    
    plt.xlim(xmin, xmax); plt.xlabel(xlabel, fontsize = 18, fontname = 'Helvetica')
    plt.ylabel(ylabel, fontsize = 18)
    ax.tick_params(axis = 'x', labelsize = 14); ax.tick_params(axis = 'y', labelsize = 14)
    ax.text(text_xpos, 0.94, textbox, transform = ax.transAxes, fontsize = 18, 
            fontname = 'Helvetica', verticalalignment = 'top', 
            horizontalalignment = 'right', bbox = props)
    
    plt.xticks(np.arange(xmin, xmax+0.01, step=round(((xmax-xmin)/(nxticks+1)),-roundx)))

    for tick in ax.get_xticklabels():
        tick.set_fontname('Helvetica')
    for tick in ax.get_yticklabels():
        tick.set_fontname('Helvetica')
    
    plt.rcParams['axes.unicode_minus'] = False
    plt.grid(); ax.set_axisbelow(True)
    plt.savefig(figure_name, dpi = 600)
    plt.show()
    
    
def plothist2(data1, data2, binwidth, textbox, xmin, xmax, xlabel, ylabel, figure_name):
    fig, ax = plt.subplots(1,1,figsize=(7,7))
    bins = np.arange(round(min(data1),1), max(data1) + binwidth, binwidth)
    props = dict(facecolor='white', alpha=1.0)
    
    ax.hist(data2, bins, edgecolor = 'black', facecolor = 'gray', alpha = 0.5)
    ax.hist(data1, bins, edgecolor = 'black', facecolor = 'blue', alpha = 0.5)
        
    plt.xlim(xmin, xmax); plt.xlabel(xlabel, fontsize = 18, fontname = 'Helvetica')
    plt.ylabel(ylabel, fontsize = 18)
    ax.tick_params(axis = 'x', labelsize = 14); ax.tick_params(axis = 'y', labelsize = 14)
#    ax.text(0.575, 0.97, textbox, transform = ax.transAxes, fontsize = 18, fontname = 'Helvetica', verticalalignment = 'top', bbox = props)
    
    for tick in ax.get_xticklabels():
        tick.set_fontname('Helvetica')
    for tick in ax.get_yticklabels():
        tick.set_fontname('Helvetica')
    
    plt.rcParams['axes.unicode_minus'] = False
    ax.rcParams['axes.grid'] = False
    plt.grid(); ax.set_axisbelow(True)
    plt.savefig(figure_name, dpi = 600)
    plt.show()


def plothist_categorical(data, ncategories, title, rotation, figure_name, xdim, ydim):
    
    fig, ax = plt.subplots(1,1,figsize=(xdim,ydim))
    
    dictionary = dict(Counter(data))
    dictionary_sorted = sorted(dictionary.items(), key=lambda kv: kv[1], reverse = True)
    dictionary_selected = dict(dictionary_sorted[0:ncategories])
    
    plt.ylabel('Counts', fontsize = 18, fontname = 'Helvetica')
    plt.tick_params(axis = 'x', labelsize = 14); ax.tick_params(axis = 'y', labelsize = 14)
    
    plt.bar(dictionary_selected.keys(), dictionary_selected.values(), edgecolor = 'black', facecolor = 'blue')
    
    plt.xlim([-0.5, ncategories-0.5])
    plt.title(title, fontsize = 20, fontname = 'Helvetica')
    
    ax.set_xticklabels(labels = dictionary_selected.keys(), rotation=rotation, ha='right')
    plt.tight_layout()

    plt.savefig(figure_name, dpi = 600)
    plt.show()
