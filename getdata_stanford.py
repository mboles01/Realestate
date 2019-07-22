#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:51:49 2019

@author: michaelboles
"""




import geopandas as gpd
shapefile_info = gpd.read_file(r'./shapefiles/Bay Zips/ZIPCODE.shp')

# get zip codes from shapefile
shapefile_info.columns
shapefile_selected = shapefile_info[['ZIP_CODE_5', 'geometry']]
shapefile_selected = shapefile_selected.rename(index = str, columns = {'ZIP_CODE_5': 'Zip'})
shapefile_zips = pd.DataFrame(shapefile_selected['Zip']).astype(int)

# get zip codes, commute time from full data set
data_bay_ziptimes = data_bay_withtimes[['Zip','Min commute']]
data_bay_ziptimes2 = data_bay_ziptimes.groupby('Zip', as_index = False).mean()#.drop(columns = 'Grade')

# get zip codes that are present in both shape file and main data set
shapefile_commute = shapefile_zips.merge(data_bay_ziptimes2, on='Zip', how='left')








import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import numpy as np

fig= plt.figure()
ax= fig.add_subplot(111)
m=Basemap(projection='cyl',llcrnrlat=34.5,llcrnrlon=19,
                           urcrnrlat=42,urcrnrlon=28.5,resolution='h')
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='w',lake_color='aqua')
m.drawcoastlines()
m.readshapefile('./shapefiles/Bay Zips/ZIPCODE.shp','shapefile')

dict1={14464: 1.16, 14465: 1.35, 14466: 1.28, 14467: 1.69, 14468: 1.81, 14418: 1.38}
colvals = dict1.values()

cmap=plt.cm.RdYlBu
norm=plt.Normalize(min(colvals),max(colvals))

patches   = []

for info, shape in zip(m.nomoi_info, m.nomoi):
    if info['ID_2'] in list(dict1.keys()):
        color=cmap(norm(dict1[info['ID_2']]))
        patches.append( Polygon(np.array(shape), True, color=color) )

pc = PatchCollection(patches, match_original=True, edgecolor='k', linewidths=1., zorder=2)
ax.add_collection(pc)

#colorbar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array(colvals)
fig.colorbar(sm, ax=ax)

plt.show()