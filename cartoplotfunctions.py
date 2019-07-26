# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:38:38 2019

@author: BolesMi
"""
# import functions
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt 
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature


# Scatter plot of color-coded prices across the bay
def cartoplot_bay_price(data, mapsize, pricequintiles, shapefile):
        
    # Create a Stamen terrain background instance
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (mapsize,mapsize))
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    
    # Set range of map, stipulate zoom level
    ax.set_extent([-122.7, -121.5, 37.15, 38.15], crs=ccrs.Geodetic())
    ax.add_image(stamen_terrain, 12, zorder = 0)
    
    # Add city borders
    shape_feature = ShapelyFeature(Reader(shapefile).geometries(), ccrs.epsg(26910), 
                               linewidth = 2, facecolor = (1, 1, 1, 0), 
                               edgecolor = (0.3, 0.3, 0.3, 1))
    ax.add_feature(shape_feature, zorder = 1)
    
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
    ax.scatter(q1["Longitude"], q1["Latitude"], s=55, zorder = 2, c="darkred", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l1)    
    ax.scatter(q2["Longitude"], q2["Latitude"], s=55, zorder = 2, c="salmon", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l2)    
    ax.scatter(q3["Longitude"], q3["Latitude"], s=55, zorder = 2, c="grey", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l3)
    ax.scatter(q4["Longitude"], q4["Latitude"], s=55, zorder = 2, c="cornflowerblue", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l4)    
    ax.scatter(q5["Longitude"], q5["Latitude"], s=55, zorder = 2, c="darkblue", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l5)    
        
    # Add text box to map
    lgnd = ax.legend(loc = 3, prop = {'family':'Helvetica', 'size': 30}, title = r"$\bf{Bay\/Area\/Home\/Prices}$", title_fontsize=33)
    
    #change the marker size manually for both lines
    lgnd.legendHandles[0]._sizes = [150]
    lgnd.legendHandles[1]._sizes = [150]
    lgnd.legendHandles[2]._sizes = [150]
    lgnd.legendHandles[3]._sizes = [150]
    lgnd.legendHandles[4]._sizes = [150]
    
    plt.show()

# Scatter plot of color-coded prices across sf
def cartoplot_sf_price(data, mapsize, pricequintiles, shapefile):
        
    # Create a Stamen terrain background instance
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (mapsize,mapsize))
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    
    # Set range of map, stipulate zoom level
    ax.set_extent([-122.55, -122.35, 37.7, 37.835], crs=ccrs.Geodetic())
    ax.add_image(stamen_terrain, 14)
    
    # Add city borders
    shape_feature = ShapelyFeature(Reader(shapefile).geometries(), ccrs.Geodetic(), 
                                   linewidth = 1, facecolor = (1, 1, 1, 0), 
                                   edgecolor = (0.3, 0.3, 0.3, 1))
    ax.add_feature(shape_feature, zorder = 1)
    
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
    ax.scatter(q1["Longitude"], q1["Latitude"], s=75, zorder = 2, c="darkred", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l1)    
    ax.scatter(q2["Longitude"], q2["Latitude"], s=75, zorder = 2, c="salmon", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l2)    
    ax.scatter(q3["Longitude"], q3["Latitude"], s=75, zorder = 2, c="grey", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l3)
    ax.scatter(q4["Longitude"], q4["Latitude"], s=75, zorder = 2, c="cornflowerblue", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l4)    
    ax.scatter(q5["Longitude"], q5["Latitude"], s=75, zorder = 2, c="darkblue", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l5)    

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
def cartoplot_eastbay_price(data, mapsize, pricequintiles, shapefile):
        
    # Create a Stamen terrain background instance
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (mapsize,mapsize))
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    
    # Set range of map, stipulate zoom level
    ax.set_extent([-122.35, -122.025, 37.725, 37.945], crs=ccrs.Geodetic())
    ax.add_image(stamen_terrain, 13)
    
    # Add city borders
    shape_feature = ShapelyFeature(Reader(shapefile).geometries(), ccrs.epsg(26910), 
                               linewidth = 1, facecolor = (1, 1, 1, 0), 
                               edgecolor = (0.3, 0.3, 0.3, 1))
    ax.add_feature(shape_feature, zorder = 1)
    
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
    ax.scatter(q1["Longitude"], q1["Latitude"], s=75, zorder = 2, c="darkred", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l1)    
    ax.scatter(q2["Longitude"], q2["Latitude"], s=75, zorder = 2, c="salmon", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l2)    
    ax.scatter(q3["Longitude"], q3["Latitude"], s=75, zorder = 2, c="grey", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l3)
    ax.scatter(q4["Longitude"], q4["Latitude"], s=75, zorder = 2, c="cornflowerblue", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l4)    
    ax.scatter(q5["Longitude"], q5["Latitude"], s=75, zorder = 2, c="darkblue", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l5)    

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
def cartoplot_peninsula_price(data, mapsize, pricequintiles, shapefile):
        
    # Create a Stamen terrain background instance
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (mapsize,mapsize))
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    
    # Set range of map, stipulate zoom level
    ax.set_extent([-122.4, -122.1, 37.4, 37.6], crs=ccrs.Geodetic())
    ax.add_image(stamen_terrain, 13)
    
    # Add city borders
    shape_feature = ShapelyFeature(Reader(shapefile).geometries(), ccrs.epsg(26910), 
                               linewidth = 1, facecolor = (1, 1, 1, 0), 
                               edgecolor = (0.3, 0.3, 0.3, 1))
    ax.add_feature(shape_feature, zorder = 1)
    
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
    ax.scatter(q1["Longitude"], q1["Latitude"], s=75, zorder = 2, c="darkred", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l1)    
    ax.scatter(q2["Longitude"], q2["Latitude"], s=75, zorder = 2, c="salmon", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l2)    
    ax.scatter(q3["Longitude"], q3["Latitude"], s=75, zorder = 2, c="grey", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l3)
    ax.scatter(q4["Longitude"], q4["Latitude"], s=75, zorder = 2, c="cornflowerblue", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l4)    
    ax.scatter(q5["Longitude"], q5["Latitude"], s=75, zorder = 2, c="darkblue", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l5)    

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
def cartoplot_southbay_price(data, mapsize, pricequintiles, shapefile):
        
    # Create a Stamen terrain background instance
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (mapsize,mapsize))
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    
    # Set range of map, stipulate zoom level
    ax.set_extent([-122.15, -121.85, 37.2, 37.4], crs=ccrs.Geodetic())
    ax.add_image(stamen_terrain, 13)
    
    # Add city borders
    shape_feature = ShapelyFeature(Reader(shapefile).geometries(), ccrs.epsg(26910), 
                               linewidth = 1, facecolor = (1, 1, 1, 0), 
                               edgecolor = (0.3, 0.3, 0.3, 1))
    ax.add_feature(shape_feature, zorder = 1)
    
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
    ax.scatter(q1["Longitude"], q1["Latitude"], s=75, zorder = 2, c="darkred", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l1)    
    ax.scatter(q2["Longitude"], q2["Latitude"], s=75, zorder = 2, c="salmon", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l2)    
    ax.scatter(q3["Longitude"], q3["Latitude"], s=75, zorder = 2, c="grey", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l3)
    ax.scatter(q4["Longitude"], q4["Latitude"], s=75, zorder = 2, c="cornflowerblue", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l4)    
    ax.scatter(q5["Longitude"], q5["Latitude"], s=75, zorder = 2, c="darkblue", edgecolors = 'black', transform=ccrs.PlateCarree(), label = l5)    

    # Add text box to map
    lgnd = ax.legend(loc = 3, prop = {'size': 25}, title = r"$\bf{South\/Bay\/\/}$", title_fontsize=30)
    
    #change the marker size manually for both lines
    lgnd.legendHandles[0]._sizes = [150]
    lgnd.legendHandles[1]._sizes = [150]
    lgnd.legendHandles[2]._sizes = [150]
    lgnd.legendHandles[3]._sizes = [150]
    lgnd.legendHandles[4]._sizes = [150]
    
    plt.show()
    
    
    
    
# Scatter plot of color-coded prices across the bay
def cartoplot_commute(data, mapsize, shapefile, commute):
        
    # Create a Stamen terrain background instance
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (mapsize,mapsize))
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    
    # Set range of map, stipulate zoom level
    ax.set_extent([-122.7, -121.5, 37.15, 38.15], crs=ccrs.Geodetic())
    ax.add_image(stamen_terrain, 10, zorder = 0)
    
    # get commute time
    commute_time = pd.read_csv(commute)
    
    # get shapefile data
    shapefile_data = pd.read_csv('./data/data by zipcode/shapefile_data.csv')
    
    # color zipcodes by commute time
    from matplotlib import cm
    import matplotlib.colors
    cmap = cm.get_cmap('seismic', 25)
    norm = matplotlib.colors.Normalize(vmin = min(commute_time['Min commute']), 
                                       vmax = max(commute_time['Min commute']))
    color = cmap(norm(commute_time['Min commute'].values))
    
    # add shapefile features
    shape_feature = ShapelyFeature(Reader(shapefile).geometries(), ccrs.epsg(26910), linewidth = 2)
    
    # Add commute data by zip code
    for counter, geom in enumerate(shape_feature.geometries()):
        if shapefile_data['AREA'][counter] < 50:
            if shapefile_data['POPULATION'][counter] > 500:
                ax.add_geometries([geom], crs=shape_feature.crs, 
                              facecolor=color[counter], edgecolor='k', alpha=0.8)
        else:
            continue
    
#    ax=plt.gca() #get the current axes
#    PCM=ax.get_children()[-8] #get the mappable, the 1st and the 2nd are the x and y axes
#    plt.colorbar(PCM,ax=ax)

#    plt.colorbar(norm)     
        
#    plt.colorbar()
    plt.show()


# Scatter plot of color-coded prices across the bay
def cartoplot_schools(data, mapsize, shapefile, schools):
        
    # Create a Stamen terrain background instance
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (mapsize,mapsize))
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    
    # Set range of map, stipulate zoom level
    ax.set_extent([-122.7, -121.5, 37.15, 38.15], crs=ccrs.Geodetic())
    ax.add_image(stamen_terrain, 10, zorder = 0)
    
    # get commute time
    commute_time = pd.read_csv(commute)
    
    # get shapefile data
    shapefile_data = pd.read_csv('./data/data by zipcode/shapefile_data.csv')
    
    # color zipcodes by commute time
    from matplotlib import cm
    import matplotlib.colors
    cmap = cm.get_cmap('seismic', 25)
    norm = matplotlib.colors.Normalize(vmin = min(commute_time['Min commute']), 
                                       vmax = max(commute_time['Min commute']))
    color = cmap(norm(commute_time['Min commute'].values))
    
    # add shapefile features
    shape_feature = ShapelyFeature(Reader(shapefile).geometries(), ccrs.epsg(26910), linewidth = 2)
    
    # Add commute data by zip code
    for counter, geom in enumerate(shape_feature.geometries()):
        if shapefile_data['AREA'][counter] < 50:
            if shapefile_data['POPULATION'][counter] > 500:
                ax.add_geometries([geom], crs=shape_feature.crs, 
                              facecolor=color[counter], edgecolor='k', alpha=0.8)
        else:
            continue
    
#    ax=plt.gca() #get the current axes
#    PCM=ax.get_children()[-8] #get the mappable, the 1st and the 2nd are the x and y axes
#    plt.colorbar(PCM,ax=ax)

#    plt.colorbar(norm)     
        
#    plt.colorbar()
    plt.show()


#
#
#shapefile_name= "./shapefiles/data/ZIPCODE.shp"
#os.path.isfile(shapefile_name) 
#mapwidth, mapheight = 8, 8
#pad = 0.25
#
#stamen_terrain = cimgt.Stamen('terrain-background')
#stm_crs = stamen_terrain.crs
#
#fig = plt.figure(figsize = (mapwidth, mapheight))
#ax = fig.add_subplot(1, 1, 1, projection=stm_crs)  #world mercator
#
## Set extent of map
#ax.set_extent([-123.3-pad, -121.5+pad, 37.05-pad, 38.75+pad], crs=ccrs.Geodetic())
## Plot base map
#ax.add_image(stamen_terrain, 8, zorder=0)
#
## Add polygons from shapefile
## Note: the use of `ccrs.epsg(26910)`
#shape_feature = ShapelyFeature(Reader(shapefile_name).geometries(), ccrs.epsg(26910))
#
## You can choose one of the 2 possible methods to plot
## ... the geometries from shapefile
## Styling is done here.
#method = 2
#if method==1:
#    # iteration is hidden
#    ax.add_feature(shape_feature, facecolor='b', edgecolor='red', 
#                   alpha=0.4, zorder = 15)
#if method==2:
#    # iterate and use `.add_geometries()`
#    # more flexible to manipulate particular items
#    for geom in shape_feature.geometries():
#        ax.add_geometries([geom], crs=shape_feature.crs, facecolor='b', 
#                          edgecolor='red', alpha=0.4)
#
#plt.show()
#
