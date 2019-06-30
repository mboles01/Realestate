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

    # Create legend labels
    l1 = '< $%s M' % str(round(pricequintiles[0]/1000000, 1))
    l2 = '\$%s M to $%s M' % (round(pricequintiles[0]/1000000, 1), round(pricequintiles[1]/1000000, 1))
    l3 = '\$%s M to $%s M' % (round(pricequintiles[1]/1000000, 1), round(pricequintiles[2]/1000000, 1))
    l4 = '\$%s M to $%s M' % (round(pricequintiles[2]/1000000, 1), round(pricequintiles[3]/1000000, 1))
    l5 = '> $%s M' % str(round(pricequintiles[3]/1000000, 1))

    # Plot scatter based on price quintiles
    ax.scatter(q1["Longitude"], q1["Latitude"], s=55, c="darkred", transform=ccrs.PlateCarree(), label = l1)    
    ax.scatter(q2["Longitude"], q2["Latitude"], s=55, c="salmon", transform=ccrs.PlateCarree(), label = l2)    
    ax.scatter(q3["Longitude"], q3["Latitude"], s=55, c="grey", transform=ccrs.PlateCarree(), label = l3)
    ax.scatter(q4["Longitude"], q4["Latitude"], s=55, c="cornflowerblue", transform=ccrs.PlateCarree(), label = l4)    
    ax.scatter(q5["Longitude"], q5["Latitude"], s=55, c="darkblue", transform=ccrs.PlateCarree(), label = l5)    
    
    # Add text box to map
    lgnd = ax.legend(loc = 3, prop = {'size': 30}, title = r"$\bf{Bay\/Area\/Home\/Prices}$", title_fontsize=33)
    
    #change the marker size manually for both lines
    lgnd.legendHandles[0]._sizes = [150]
    lgnd.legendHandles[1]._sizes = [150]
    lgnd.legendHandles[2]._sizes = [150]
    lgnd.legendHandles[3]._sizes = [150]
    lgnd.legendHandles[4]._sizes = [150]
    
    plt.show()

# Scatter plot of color-coded prices across sf
def cartoplot_sf_price(data, mapsize, pricequintiles):
        
    # Create a Stamen terrain background instance
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (mapsize,mapsize))
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    
    # Set range of map, stipulate zoom level
    ax.set_extent([-122.55, -122.35, 37.7, 37.835], crs=ccrs.Geodetic())
    ax.add_image(stamen_terrain, 14)
    
    # Determine plotting mode and subdivide data based on quintiles
    q1 = data.loc[data["Price"] < pricequintiles[0]]
    q2 = data.loc[(data["Price"] > pricequintiles[0]) & (data["Price"] < pricequintiles[1])]
    q3 = data.loc[(data["Price"] > pricequintiles[1]) & (data["Price"] < pricequintiles[2])]
    q4 = data.loc[(data["Price"] > pricequintiles[2]) & (data["Price"] < pricequintiles[3])]
    q5 = data.loc[data["Price"] > pricequintiles[3]]
    
    # Create legend labels
    l1 = '< $%s M' % str(round(pricequintiles[0]/1000000, 2))
    l2 = '\$%s M to $%s M' % (round(pricequintiles[0]/1000000, 2), round(pricequintiles[1]/1000000, 2))
    l3 = '\$%s M to $%s M' % (round(pricequintiles[1]/1000000, 2), round(pricequintiles[2]/1000000, 2))
    l4 = '\$%s M to $%s M' % (round(pricequintiles[2]/1000000, 2), round(pricequintiles[3]/1000000, 2))
    l5 = '> $%s M' % str(round(pricequintiles[3]/1000000, 2))

    # Plot scatter based on price quintiles
    ax.scatter(q1["Longitude"], q1["Latitude"], s=75, c="darkred", transform=ccrs.PlateCarree(), label = l1)    
    ax.scatter(q2["Longitude"], q2["Latitude"], s=75, c="salmon", transform=ccrs.PlateCarree(), label = l2)    
    ax.scatter(q3["Longitude"], q3["Latitude"], s=75, c="grey", transform=ccrs.PlateCarree(), label = l3)
    ax.scatter(q4["Longitude"], q4["Latitude"], s=75, c="cornflowerblue", transform=ccrs.PlateCarree(), label = l4)    
    ax.scatter(q5["Longitude"], q5["Latitude"], s=75, c="darkblue", transform=ccrs.PlateCarree(), label = l5)    

    # Add text box to map
    lgnd = ax.legend(loc = 2, prop = {'size': 25}, title = r"$\bf{San\/Francisco\/\/}$", title_fontsize=30)
    
    #change the marker size manually for both lines
    lgnd.legendHandles[0]._sizes = [150]
    lgnd.legendHandles[1]._sizes = [150]
    lgnd.legendHandles[2]._sizes = [150]
    lgnd.legendHandles[3]._sizes = [150]
    lgnd.legendHandles[4]._sizes = [150]
    
    plt.show()


# Scatter plot of color-coded prices across east bay
def cartoplot_eastbay_price(data, mapsize, pricequintiles):
        
    # Create a Stamen terrain background instance
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (mapsize,mapsize))
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    
    # Set range of map, stipulate zoom level
    ax.set_extent([-122.35, -122.025, 37.725, 37.945], crs=ccrs.Geodetic())
    ax.add_image(stamen_terrain, 13)
    
    # Determine plotting mode and subdivide data based on quintiles
    q1 = data.loc[data["Price"] < pricequintiles[0]]
    q2 = data.loc[(data["Price"] > pricequintiles[0]) & (data["Price"] < pricequintiles[1])]
    q3 = data.loc[(data["Price"] > pricequintiles[1]) & (data["Price"] < pricequintiles[2])]
    q4 = data.loc[(data["Price"] > pricequintiles[2]) & (data["Price"] < pricequintiles[3])]
    q5 = data.loc[data["Price"] > pricequintiles[3]]

    # Create legend labels
    l1 = '< $%s M' % str(round(pricequintiles[0]/1000000, 1))
    l2 = '\$%s M to $%s M' % (round(pricequintiles[0]/1000000, 1), round(pricequintiles[1]/1000000, 1))
    l3 = '\$%s M to $%s M' % (round(pricequintiles[1]/1000000, 1), round(pricequintiles[2]/1000000, 1))
    l4 = '\$%s M to $%s M' % (round(pricequintiles[2]/1000000, 1), round(pricequintiles[3]/1000000, 1))
    l5 = '> $%s M' % str(round(pricequintiles[3]/1000000, 1))

    # Plot scatter based on price quintiles
    ax.scatter(q1["Longitude"], q1["Latitude"], s=75, c="darkred", transform=ccrs.PlateCarree(), label = l1)    
    ax.scatter(q2["Longitude"], q2["Latitude"], s=75, c="salmon", transform=ccrs.PlateCarree(), label = l2)    
    ax.scatter(q3["Longitude"], q3["Latitude"], s=75, c="grey", transform=ccrs.PlateCarree(), label = l3)
    ax.scatter(q4["Longitude"], q4["Latitude"], s=75, c="cornflowerblue", transform=ccrs.PlateCarree(), label = l4)    
    ax.scatter(q5["Longitude"], q5["Latitude"], s=75, c="darkblue", transform=ccrs.PlateCarree(), label = l5)    

    # Add text box to map
    lgnd = ax.legend(loc = 4, prop = {'size': 25}, title = r"$\bf{East\/Bay\/\/}$", title_fontsize=30)
    
    #change the marker size manually for both lines
    lgnd.legendHandles[0]._sizes = [150]
    lgnd.legendHandles[1]._sizes = [150]
    lgnd.legendHandles[2]._sizes = [150]
    lgnd.legendHandles[3]._sizes = [150]
    lgnd.legendHandles[4]._sizes = [150]
    
    plt.show()

# Scatter plot of color-coded prices across peninsula
def cartoplot_peninsula_price(data, mapsize, pricequintiles):
        
    # Create a Stamen terrain background instance
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (mapsize,mapsize))
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    
    # Set range of map, stipulate zoom level
    ax.set_extent([-122.4, -122.1, 37.4, 37.6], crs=ccrs.Geodetic())
    ax.add_image(stamen_terrain, 13)
    
    # Determine plotting mode and subdivide data based on quintiles
    q1 = data.loc[data["Price"] < pricequintiles[0]]
    q2 = data.loc[(data["Price"] > pricequintiles[0]) & (data["Price"] < pricequintiles[1])]
    q3 = data.loc[(data["Price"] > pricequintiles[1]) & (data["Price"] < pricequintiles[2])]
    q4 = data.loc[(data["Price"] > pricequintiles[2]) & (data["Price"] < pricequintiles[3])]
    q5 = data.loc[data["Price"] > pricequintiles[3]]

    # Create legend labels
    l1 = '< $%s M' % str(round(pricequintiles[0]/1000000, 1))
    l2 = '\$%s M to $%s M' % (round(pricequintiles[0]/1000000, 1), round(pricequintiles[1]/1000000, 1))
    l3 = '\$%s M to $%s M' % (round(pricequintiles[1]/1000000, 1), round(pricequintiles[2]/1000000, 1))
    l4 = '\$%s M to $%s M' % (round(pricequintiles[2]/1000000, 1), round(pricequintiles[3]/1000000, 1))
    l5 = '> $%s M' % str(round(pricequintiles[3]/1000000, 1))

    # Plot scatter based on price quintiles
    ax.scatter(q1["Longitude"], q1["Latitude"], s=75, c="darkred", transform=ccrs.PlateCarree(), label = l1)    
    ax.scatter(q2["Longitude"], q2["Latitude"], s=75, c="salmon", transform=ccrs.PlateCarree(), label = l2)    
    ax.scatter(q3["Longitude"], q3["Latitude"], s=75, c="grey", transform=ccrs.PlateCarree(), label = l3)
    ax.scatter(q4["Longitude"], q4["Latitude"], s=75, c="cornflowerblue", transform=ccrs.PlateCarree(), label = l4)    
    ax.scatter(q5["Longitude"], q5["Latitude"], s=75, c="darkblue", transform=ccrs.PlateCarree(), label = l5)    

    # Add text box to map
    lgnd = ax.legend(loc = 3, prop = {'size': 25}, title = r"$\bf{Peninsula\/\/}$", title_fontsize=30)
    
    #change the marker size manually for both lines
    lgnd.legendHandles[0]._sizes = [150]
    lgnd.legendHandles[1]._sizes = [150]
    lgnd.legendHandles[2]._sizes = [150]
    lgnd.legendHandles[3]._sizes = [150]
    lgnd.legendHandles[4]._sizes = [150]
    
    plt.show()

# Scatter plot of color-coded prices across south bay
def cartoplot_southbay_price(data, mapsize, pricequintiles):
        
    # Create a Stamen terrain background instance
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (mapsize,mapsize))
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    
    # Set range of map, stipulate zoom level
    ax.set_extent([-122.15, -121.85, 37.2, 37.4], crs=ccrs.Geodetic())
    ax.add_image(stamen_terrain, 13)
    
    # Determine plotting mode and subdivide data based on quintiles
    q1 = data.loc[data["Price"] < pricequintiles[0]]
    q2 = data.loc[(data["Price"] > pricequintiles[0]) & (data["Price"] < pricequintiles[1])]
    q3 = data.loc[(data["Price"] > pricequintiles[1]) & (data["Price"] < pricequintiles[2])]
    q4 = data.loc[(data["Price"] > pricequintiles[2]) & (data["Price"] < pricequintiles[3])]
    q5 = data.loc[data["Price"] > pricequintiles[3]]

    # Create legend labels
    l1 = '< $%s M' % str(round(pricequintiles[0]/1000000, 1))
    l2 = '\$%s M to $%s M' % (round(pricequintiles[0]/1000000, 1), round(pricequintiles[1]/1000000, 1))
    l3 = '\$%s M to $%s M' % (round(pricequintiles[1]/1000000, 1), round(pricequintiles[2]/1000000, 1))
    l4 = '\$%s M to $%s M' % (round(pricequintiles[2]/1000000, 1), round(pricequintiles[3]/1000000, 1))
    l5 = '> $%s M' % str(round(pricequintiles[3]/1000000, 1))

    # Plot scatter based on price quintiles
    ax.scatter(q1["Longitude"], q1["Latitude"], s=75, c="darkred", transform=ccrs.PlateCarree(), label = l1)    
    ax.scatter(q2["Longitude"], q2["Latitude"], s=75, c="salmon", transform=ccrs.PlateCarree(), label = l2)    
    ax.scatter(q3["Longitude"], q3["Latitude"], s=75, c="grey", transform=ccrs.PlateCarree(), label = l3)
    ax.scatter(q4["Longitude"], q4["Latitude"], s=75, c="cornflowerblue", transform=ccrs.PlateCarree(), label = l4)    
    ax.scatter(q5["Longitude"], q5["Latitude"], s=75, c="darkblue", transform=ccrs.PlateCarree(), label = l5)    

    # Add text box to map
    lgnd = ax.legend(loc = 3, prop = {'size': 25}, title = r"$\bf{South\/Bay\/\/}$", title_fontsize=30)
    
    #change the marker size manually for both lines
    lgnd.legendHandles[0]._sizes = [150]
    lgnd.legendHandles[1]._sizes = [150]
    lgnd.legendHandles[2]._sizes = [150]
    lgnd.legendHandles[3]._sizes = [150]
    lgnd.legendHandles[4]._sizes = [150]
    
    plt.show()
