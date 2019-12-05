#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 16:43:36 2019

@author: michaelboles
"""

# set up working directory
import os
#os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate/Data/ABB') # Mac
os.chdir('/Users/bolesmi/Lam/Coding/Python/2019/Realestate/Data/ABB') # PC

# import standard packages
import numpy as np
import pandas as pd

# import cleaned SF listing dataset with bag of words (bow) or term freq inv doc freq (tfidf) vectors
listings_bow = pd.read_csv('./Data/Clean/San_Francisco/listings_sf_data_bow.csv', 
                           compression='gzip')

listings_tfidf = pd.read_csv('./Data/Clean/San_Francisco/listings_sf_data_tfidf.csv', 
                           compression='gzip')

# encode each revenue category with number
encoded = ['Low', 'High']
revenue_category = pd.DataFrame({'revenue_category': encoded, 
                            'revenue_category_code': list(range(len(encoded)))})

# separate into high- and low-revenue categories
listings_bow_highlow = listings_bow[listings_bow['revenue_category'] != 'Medium']
listings_tfidf_highlow = listings_tfidf[listings_tfidf['revenue_category'] != 'Medium']

# merge revenue code with selected data
listings_bow_highlow_encoded = revenue_category.merge(listings_bow_highlow, on='revenue_category', how='left')
listings_tfidf_highlow_encoded = revenue_category.merge(listings_tfidf_highlow, on='revenue_category', how='left')

# stipulate x- and y-variables

## for simple PCA plot of bow or tfidf vectors
#X = listings_bow_highlow.iloc[:,4:]
#y = listings_bow_highlow['revenue_category']
#
#X = listings_tfidf_highlow.iloc[:,4:]
#y = listings_tfidf_highlow['revenue_category']

# encoded for classification 
X = listings_bow_highlow_encoded.iloc[:,5:]
y = listings_bow_highlow_encoded['revenue_category_code']

X = listings_tfidf_highlow_encoded.iloc[:,5:]
y = listings_tfidf_highlow_encoded['revenue_category_code']

# split into train and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)



### ANALYSIS ###


### PCA - component axes that maximize explained variance - unsupervised, no consideration of dependent variable ###

# apply principal component analysis (PCA)
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
X_pca = pca.fit_transform(X)
explained_variance = pca.explained_variance_ratio_

# Logistic regression

# fit logistic regression to training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0, solver='lbfgs', max_iter = 2000)
classifier.fit(X_train, y_train)

# get coefficients
coefficients = pd.concat([pd.DataFrame(X.columns),pd.DataFrame(np.transpose(classifier.coef_))], axis = 1)
coefficients.columns = ['Word', 'Coefficient']
lowrev_topten = coefficients.sort_values(by=['Coefficient'])[:10]
highrev_topten = coefficients.sort_values(by=['Coefficient'], ascending=False)[:10]

# predict test set results
y_pred = classifier.predict(X_test)

# create confusion matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
cm_df = pd.DataFrame(cm, index = ['Low', 'High'], columns = ['Low', 'High'])
score = accuracy_score(y_test, y_pred)






### PLOTTING ###

# visualize PCA result
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
x_set, y_set = X_pca, y
x1, x2 = np.meshgrid(np.arange(start = x_set[:, 0].min() - 1, 
                               stop = x_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = x_set[:, 1].min() - 1, 
                               stop = x_set[:, 1].max() + 1, step = 0.01))
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
                c = ListedColormap(('blue', 'red'))(i), label = j,
                s = .5)
plt.title('PCA: high- vs. low-revenue Airbnbs \n using listing text tf-idf vector')
#plt.xlim(-0.15, 0.15)
#plt.ylim(-0.25, 0.4)
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.legend(markerscale = 10)
#plt.savefig('./Images/NLP/PCA_Airbnb_text_tfidf_nozoom.jpg', bbox_inches='tight', dpi = 600) 
plt.show()

# plot confusion matrix
import seaborn as sns
plt.figure(figsize = (5,5))
sns.heatmap(cm_df, annot=True, annot_kws={"size": 20}, fmt="d", cmap="YlGnBu", 
            cbar=False, linecolor = 'black', linewidths=.5)
plt.title('Airbnb revenue category prediction from \n listing text with tfidf (accuracy: %s)' % round(score,3), fontsize=14)
plt.xlabel('Predicted label', fontsize=14)
plt.ylabel('True label', fontsize=14)
plt.savefig('./Images/NLP/Confusion_matrix_tfidf.jpg', bbox_inches='tight', dpi = 600) 

# plot word importance bar graphs
fig, axes = plt.subplots(1,2,figsize=(5,10))
plt.subplots_adjust(wspace = 1)

axes[0].set_title('Low revenue')
axes[0].invert_yaxis()
axes[0].barh(np.arange(len(lowrev_topten)), lowrev_topten['Coefficient'])
axes[0].set_yticklabels(list(lowrev_topten['Word']))
axes[0].set_xlabel('Coefficient')
axes[0].set_yticks(np.arange(0,10))

axes[1].set_title('High revenue')
axes[1].invert_yaxis()
axes[1].barh(np.arange(len(highrev_topten)), highrev_topten['Coefficient'])
axes[1].set_yticklabels(list(highrev_topten['Word']))
axes[1].set_xlabel('Coefficient')
axes[1].set_yticks(np.arange(0,10))

plt.savefig('./Images/NLP/Word_rank_tfidf.jpg', bbox_inches='tight', dpi = 600) 















### COMBINED WORD ANALYSIS ACROSS LISTINGS ###

# create word frequency dictionary across all listings
from nlp_functions import count_words
listings_wordcount = count_words(listings_text9)

# sort word frequency dictionary
import operator
listings_wordcount_sorted = sorted(listings_wordcount.items(),key=operator.itemgetter(1),reverse=True)
df_listings_wordcount_sorted = pd.DataFrame(data = listings_wordcount_sorted, columns =['Word', 'Count'])






















### PLOT HISTOGRAMS - NUMERICAL ###

# revenue estimates

histogram_text = texthist(data = listings_sf_clean['monthly_revenue'], 
                          divide_median=1, divide_stdev=1, rounding=0,
                          decimals = 0, units = '', dollars = True)

name = './Images/monthly_revenue.jpg'
plothist(data = listings_sf_clean['monthly_revenue'], nbins = 35, nxticks = 6, roundx = 3, 
         textbox = histogram_text, text_xpos = .94, xmin = 0, xmax = 20000, shift = None,
         xlabel = 'Revenue per month ($)', ylabel = 'Counts', figure_name = name)



### PLOT HISTOGRAMS - CATEGORICAL ###

# property type

name = './Images/property_type.jpg'

plothist_categorical(data = listings_sf_clean['property_type'], ncategories = 7, 
                     title = 'Property type', rotation = 45, figure_name = name,
                     xdim = 7, ydim = 7)


