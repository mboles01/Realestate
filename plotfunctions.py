# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:38:38 2019

@author: BolesMi
"""

# plot map, plot coordinates on top of map
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt

def cartoplot_bay(long, lat, color, mincolor, maxcolor):
    # Create a Stamen terrain background instance.
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (10,10))
    # Create a GeoAxes in the tile's projection.
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    # Limit the extent of the map to a small longitude/latitude range.
    ax.set_extent([-122.7, -121.5, 37.15, 38.15], crs=ccrs.Geodetic())
    # Add the Stamen data at given zoom level
    ax.add_image(stamen_terrain, 12)
    ax.scatter(long, lat, s=5, c=color, cmap='bwr', vmin=mincolor, vmax=maxcolor, transform=ccrs.PlateCarree())
    plt.show()


def cartoplot_sf(long, lat):
    # Create a Stamen terrain background instance.
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (10,10))
    # Create a GeoAxes in the tile's projection.
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    # Limit the extent of the map to a small longitude/latitude range.
    ax.set_extent([-122.55, -122.35, 37.7, 37.825], crs=ccrs.Geodetic())
    # Add the Stamen data at given zoom level
    ax.add_image(stamen_terrain, 14)
    ax.scatter(long, lat, s=5, c='r',transform=ccrs.PlateCarree())
    plt.show()


def cartoplot_eastbay(long, lat):
    # Create a Stamen terrain background instance.
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (10,10))
    # Create a GeoAxes in the tile's projection.
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    # Limit the extent of the map to a small longitude/latitude range.
    ax.set_extent([-122.35, -122.025, 37.75, 37.925], crs=ccrs.Geodetic())
    # Add the Stamen data at given zoom level.
    ax.add_image(stamen_terrain, 13)
    ax.scatter(long, lat, s=5, c='r',transform=ccrs.PlateCarree())
    plt.show()
    
    
def cartoplot_southbay(long, lat):
    # Create a Stamen terrain background instance.
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (10,10))
    # Create a GeoAxes in the tile's projection.
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    # Limit the extent of the map to a small longitude/latitude range.
    ax.set_extent([-122.15, -121.75, 37.2, 37.45], crs=ccrs.Geodetic())
    # Add the Stamen data at given zoom level.
    ax.add_image(stamen_terrain, 13)
    ax.scatter(long, lat, s=5, c='r',transform=ccrs.PlateCarree())
    plt.show()