# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:38:38 2019

@author: BolesMi
"""
# import functions
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt


# Scatter plot of color-coded prices across the bay
def cartoplot_bay_price(data, mapsize, pricequintiles):
        
    # Create a Stamen terrain background instance
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (mapsize,mapsize))
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    
    # Set range of map, stipulate zoom level
    ax.set_extent([-122.7, -121.5, 37.15, 38.15], crs=ccrs.Geodetic())
    ax.add_image(stamen_terrain, 12)
    
    # Determine plotting mode and subdivide data based on quintiles
    q1 = data.loc[data["Price"] < pricequintiles[0]]
    q2 = data.loc[(data["Price"] > pricequintiles[0]) & (data["Price"] < pricequintiles[1])]
    q3 = data.loc[(data["Price"] > pricequintiles[1]) & (data["Price"] < pricequintiles[2])]
    q4 = data.loc[(data["Price"] > pricequintiles[2]) & (data["Price"] < pricequintiles[3])]
    q5 = data.loc[data["Price"] > pricequintiles[3]]

    # Plot scatter based on price quintiles
    ax.scatter(q1["Longitude"], q1["Latitude"], s=15, c="darkred", transform=ccrs.PlateCarree())    
    ax.scatter(q2["Longitude"], q2["Latitude"], s=15, c="salmon", transform=ccrs.PlateCarree())    
    ax.scatter(q3["Longitude"], q3["Latitude"], s=15, c="grey", transform=ccrs.PlateCarree())
    ax.scatter(q4["Longitude"], q4["Latitude"], s=15, c="cornflowerblue", transform=ccrs.PlateCarree())    
    ax.scatter(q5["Longitude"], q5["Latitude"], s=15, c="darkblue", transform=ccrs.PlateCarree())    
    plt.show()
    
    
# Scatter plot of color-coded prices across the bay
def cartoplot_bay_pricepersqft(data, mapsize, pricepersqftquintiles):
        
    # Create a Stamen terrain background instance
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (mapsize,mapsize))
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    
    # Set range of map, stipulate zoom level
    ax.set_extent([-122.7, -121.5, 37.15, 38.15], crs=ccrs.Geodetic())
    ax.add_image(stamen_terrain, 12)
    
    # Determine plotting mode and subdivide data based on quintiles
    q1 = data.loc[data["Price per sqft"] < pricepersqftquintiles[0]]
    q2 = data.loc[(data["Price per sqft"] > pricepersqftquintiles[0]) & (data["Price per sqft"] < pricepersqftquintiles[1])]
    q3 = data.loc[(data["Price per sqft"] > pricepersqftquintiles[1]) & (data["Price per sqft"] < pricepersqftquintiles[2])]
    q4 = data.loc[(data["Price per sqft"] > pricepersqftquintiles[2]) & (data["Price per sqft"] < pricepersqftquintiles[3])]
    q5 = data.loc[data["Price per sqft"] > pricepersqftquintiles[3]]
    
    # Plot scatter based on price quintiles
    ax.scatter(q1["Longitude"], q1["Latitude"], s=15, c="darkred", transform=ccrs.PlateCarree())    
    ax.scatter(q2["Longitude"], q2["Latitude"], s=15, c="salmon", transform=ccrs.PlateCarree())    
    ax.scatter(q3["Longitude"], q3["Latitude"], s=15, c="grey", transform=ccrs.PlateCarree())
    ax.scatter(q4["Longitude"], q4["Latitude"], s=15, c="cornflowerblue", transform=ccrs.PlateCarree())    
    ax.scatter(q5["Longitude"], q5["Latitude"], s=15, c="darkblue", transform=ccrs.PlateCarree())    
    plt.show()

    
# Scatter plot of color-coded prices across the bay
def cartoplot_bay_priceperlotsqft(data, mapsize, priceperlotsqftquintiles):
        
    # Create a Stamen terrain background instance
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (mapsize,mapsize))
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    
    # Set range of map, stipulate zoom level
    ax.set_extent([-122.7, -121.5, 37.15, 38.15], crs=ccrs.Geodetic())
    ax.add_image(stamen_terrain, 12)
    
    # Determine plotting mode and subdivide data based on quintiles
    q1 = data.loc[data["Price per lot sqft"] < priceperlotsqftquintiles[0]]
    q2 = data.loc[(data["Price per lot sqft"] > priceperlotsqftquintiles[0]) & (data["Price per lot sqft"] < priceperlotsqftquintiles[1])]
    q3 = data.loc[(data["Price per lot sqft"] > priceperlotsqftquintiles[1]) & (data["Price per lot sqft"] < priceperlotsqftquintiles[2])]
    q4 = data.loc[(data["Price per lot sqft"] > priceperlotsqftquintiles[2]) & (data["Price per lot sqft"] < priceperlotsqftquintiles[3])]
    q5 = data.loc[data["Price per lot sqft"] > priceperlotsqftquintiles[3]]
    
    # Plot scatter based on price quintiles
    ax.scatter(q1["Longitude"], q1["Latitude"], s=15, c="darkred", transform=ccrs.PlateCarree())    
    ax.scatter(q2["Longitude"], q2["Latitude"], s=15, c="salmon", transform=ccrs.PlateCarree())    
    ax.scatter(q3["Longitude"], q3["Latitude"], s=15, c="grey", transform=ccrs.PlateCarree())
    ax.scatter(q4["Longitude"], q4["Latitude"], s=15, c="cornflowerblue", transform=ccrs.PlateCarree())    
    ax.scatter(q5["Longitude"], q5["Latitude"], s=15, c="darkblue", transform=ccrs.PlateCarree())    
    plt.show()    

    

# Scatter plot of color-coded prices across the sf
def cartoplot_sf_price(data, mapsize, pricequintiles):
        
    # Create a Stamen terrain background instance
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (mapsize,mapsize))
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    
    # Set range of map, stipulate zoom level
    ax.set_extent([-122.55, -122.35, 37.7, 37.825], crs=ccrs.Geodetic())
    ax.add_image(stamen_terrain, 14)
    
    # Determine plotting mode and subdivide data based on quintiles
    q1 = data.loc[data["Price"] < pricequintiles[0]]
    q2 = data.loc[(data["Price"] > pricequintiles[0]) & (data["Price"] < pricequintiles[1])]
    q3 = data.loc[(data["Price"] > pricequintiles[1]) & (data["Price"] < pricequintiles[2])]
    q4 = data.loc[(data["Price"] > pricequintiles[2]) & (data["Price"] < pricequintiles[3])]
    q5 = data.loc[data["Price"] > pricequintiles[3]]

    # Plot scatter based on price quintiles
    ax.scatter(q1["Longitude"], q1["Latitude"], s=15, c="darkred", transform=ccrs.PlateCarree())    
    ax.scatter(q2["Longitude"], q2["Latitude"], s=15, c="salmon", transform=ccrs.PlateCarree())    
    ax.scatter(q3["Longitude"], q3["Latitude"], s=15, c="grey", transform=ccrs.PlateCarree())
    ax.scatter(q4["Longitude"], q4["Latitude"], s=15, c="cornflowerblue", transform=ccrs.PlateCarree())    
    ax.scatter(q5["Longitude"], q5["Latitude"], s=15, c="darkblue", transform=ccrs.PlateCarree())    
    plt.show()


def cartoplot_eastbay(long, lat, color, mincolor, maxcolor, size):
    # Create a Stamen terrain background instance.
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (10,10))
    # Create a GeoAxes in the tile's projection.
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    # Limit the extent of the map to a small longitude/latitude range.
    ax.set_extent([-122.35, -122.025, 37.75, 37.925], crs=ccrs.Geodetic())
    # Add the Stamen data at given zoom level.
    ax.add_image(stamen_terrain, 13)
    ax.scatter(long, lat, s=5, c=color, cmap='bwr', vmin=mincolor, vmax=maxcolor, transform=ccrs.PlateCarree())
    plt.show()
    
    
def cartoplot_southbay(long, lat, color, mincolor, maxcolor, size):
    # Create a Stamen terrain background instance.
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (10,10))
    # Create a GeoAxes in the tile's projection.
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    # Limit the extent of the map to a small longitude/latitude range.
    ax.set_extent([-122.15, -121.75, 37.2, 37.45], crs=ccrs.Geodetic())
    # Add the Stamen data at given zoom level.
    ax.add_image(stamen_terrain, 13)
    ax.scatter(long, lat, s=5, c=color, cmap='bwr', vmin=mincolor, vmax=maxcolor,transform=ccrs.PlateCarree())
    plt.show()