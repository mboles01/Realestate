# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:38:38 2019

@author: BolesMi
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt

def cartoplot(longmin, longmax, latmin, latmax, zoom):
    # Create a Stamen terrain background instance.
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (10,10))
    # Create a GeoAxes in the tile's projection.
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    # Limit the extent of the map to a small longitude/latitude range.
    ax.set_extent([longmin, longmax, latmin, latmax], crs=ccrs.Geodetic())
    # Add the Stamen data at zoom level 8.
    ax.add_image(stamen_terrain, zoom)
    plt.show()
    
bayarea = cartoplot(-122.7, -121.5, 37.15, 38.15, 12)
sf = cartoplot(-122.55, -122.35, 37.7, 37.825, 14)
