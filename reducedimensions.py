# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 13:21:30 2019

@author: BolesMi
"""

# set up working directory
import os
#os.chdir('/Users/michaelboles/Michael/Coding/2019/Realestate') # Mac
os.chdir('C:\\Users\\bolesmi\\Lam\\Coding\\Python\\2019\\Realestate') # PC

# import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import full dataset 
data_all_raw = pd.read_csv('./Data/listings/data_all_price_predictions.csv')
data_all_raw.columns

# pull out columns of interest
data_subset = data_all_raw[['City', 'Beds', 'Baths', 'Home_size', 'Lot_size', 'School_score', 'Commute_time', 'Price']]

# count number of entries for each city/town
city_counts = data_subset.groupby('City').count().iloc[:,2].to_frame()
city_counts.columns = ['Count']
city_counts_sorted = city_counts.sort_values('Count', ascending = False)

# choose cities to examine for PCA / LDA classification 
trio1 = ['San Francisco', 'San Jose', 'Oakland'] # PCA 82% / LDA 88% accurate
trio2 = ['San Francisco', 'Palo Alto', 'Orinda'] # PCA 93% / LDA 99% accurate
trio3 = ['San Francisco', 'San Mateo', 'Tiburon'] # PCA 84% / LDA 90% accurate
trio4 = ['San Francisco', 'San Jose', 'Vallejo'] # PCA 93% / LDA 99% accurate

cities_of_interest = trio1
cities_of_interest.sort()

# create dataframe with only cities of interest
data_of_interest = data_subset[data_subset['City'].isin(cities_of_interest)].sort_values('City')

# encode each city of interest with number
city_number = pd.DataFrame({'City': cities_of_interest, 
                            'City code': list(range(len(cities_of_interest)))})

# merge city numbers with selected data
data_citynumbers = city_number.merge(data_of_interest, on='City', how='left')

# stipulate x- and y-variables
x = data_citynumbers[['Beds', 'Baths', 'Home_size', 'Lot_size', 'School_score', 'Commute_time', 'Price']]
y = data_citynumbers['City code']

# split into train and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

### PCA - component axes that maximize explained variance - unsupervised, no consideration of dependent variable ###

## apply principal component analysis (PCA)
#from sklearn.decomposition import PCA
#pca = PCA(n_components = 2)
#x_train = pca.fit_transform(x_train)
#x_test = pca.transform(x_test)
#explained_variance = pca.explained_variance_ratio_

### LDA - component axes that maximize class separation - supervised, considers dependent variable ### 

# apply linear discriminant analysis (LDA)
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
lda = LDA(n_components = 2)
x_train = lda.fit_transform(x_train, y_train)
x_test = lda.transform(x_test)

# fit logistic regression to training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0, solver='lbfgs')
classifier.fit(x_train, y_train)

# predict test set results
y_pred = classifier.predict(x_test)

# create confusion matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
score = accuracy_score(y_test, y_pred)

# visualize training set results
from matplotlib.colors import ListedColormap
x_set, y_set = x_train, y_train
x1, x2 = np.meshgrid(np.arange(start = x_set[:, 0].min() - 1, 
                               stop = x_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = x_set[:, 1].min() - 1, 
                               stop = x_set[:, 1].max() + 1, step = 0.01))

plt.contourf(x1, x2, classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
             alpha = 0.5, cmap = ListedColormap(('red', 'green', 'blue')))
plt.xlim(x1.min(), x1.max())
plt.ylim(x2.min(), x2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
                c = ListedColormap(('red', 'green', 'blue'))(i), label = j,
                edgecolors = 'black', s = 10)
plt.title('Logistic regression - training set')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
#plt.xlabel('Dimension 1 (%s%%)' % str(int(explained_variance[0]*100)))
#plt.ylabel('Dimension 2 (%s%%)' % str(int(explained_variance[1]*100)))
#plt.savefig('PCA_train.jpg', bbox_inches='tight', dpi = 400) 
plt.show()

# visualize test set results
from matplotlib.colors import ListedColormap
x_set, y_set = x_test, y_test
x1, x2 = np.meshgrid(np.arange(start = x_set[:, 0].min() - 1, 
                               stop = x_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = x_set[:, 1].min() - 1, 
                               stop = x_set[:, 1].max() + 1, step = 0.01))

plt.contourf(x1, x2, classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
             alpha = 0.5, cmap = ListedColormap(('red', 'green', 'blue')))
plt.xlim(x1.min(), x1.max())
plt.ylim(x2.min(), x2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
                c = ListedColormap(('red', 'green', 'blue'))(i), label = j,
                edgecolors = 'black', s = 10)
plt.title('Logistic regression - test set')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
#plt.savefig('PCA_test.jpg', bbox_inches='tight', dpi = 400) 
plt.show()










