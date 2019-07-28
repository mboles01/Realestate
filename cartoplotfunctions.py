# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:38:38 2019

@author: BolesMi
"""
# import functions
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
    q1 = data.loc[data['Price'] < pricequintiles[0]]
    q2 = data.loc[(data['Price'] > pricequintiles[0]) & (data['Price'] < pricequintiles[1])]
    q3 = data.loc[(data['Price'] > pricequintiles[1]) & (data['Price'] < pricequintiles[2])]
    q4 = data.loc[(data['Price'] > pricequintiles[2]) & (data['Price'] < pricequintiles[3])]
    q5 = data.loc[data['Price'] > pricequintiles[3]]

    # Create legend labels
    l1 = '< $%s M' % str(round(pricequintiles[0]/1000000, 1))
    l2 = '\$%s M to $%s M' % (round(pricequintiles[0]/1000000, 1), round(pricequintiles[1]/1000000, 1))
    l3 = '\$%s M to $%s M' % (round(pricequintiles[1]/1000000, 1), round(pricequintiles[2]/1000000, 1))
    l4 = '\$%s M to $%s M' % (round(pricequintiles[2]/1000000, 1), round(pricequintiles[3]/1000000, 1))
    l5 = '> $%s M' % str(round(pricequintiles[3]/1000000, 1))

    # Plot scatter based on price quintiles
    ax.scatter(q1['Longitude'], q1['Latitude'], s=55, zorder = 2, c='darkred', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l1)    
    ax.scatter(q2['Longitude'], q2['Latitude'], s=55, zorder = 2, c='salmon', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l2)    
    ax.scatter(q3['Longitude'], q3['Latitude'], s=55, zorder = 2, c='grey', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l3)
    ax.scatter(q4['Longitude'], q4['Latitude'], s=55, zorder = 2, c='cornflowerblue', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l4)    
    ax.scatter(q5['Longitude'], q5['Latitude'], s=55, zorder = 2, c='darkblue', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l5)    
        
    # Add text box to map
    lgnd = ax.legend(loc = 3, prop = {'family':'Helvetica', 'size': 30}, title = r'$\bf{Bay\/Area\/Home\/Prices}$', title_fontsize=33)
    
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
    q1 = data.loc[data['Price'] < pricequintiles[0]]
    q2 = data.loc[(data['Price'] > pricequintiles[0]) & (data['Price'] < pricequintiles[1])]
    q3 = data.loc[(data['Price'] > pricequintiles[1]) & (data['Price'] < pricequintiles[2])]
    q4 = data.loc[(data['Price'] > pricequintiles[2]) & (data['Price'] < pricequintiles[3])]
    q5 = data.loc[data['Price'] > pricequintiles[3]]
    
    # Create legend labels
    l1 = '< $%s M' % str(round(pricequintiles[0]/1000000, 2))
    l2 = '\$%s M to $%s M' % (round(pricequintiles[0]/1000000, 2), round(pricequintiles[1]/1000000, 2))
    l3 = '\$%s M to $%s M' % (round(pricequintiles[1]/1000000, 2), round(pricequintiles[2]/1000000, 2))
    l4 = '\$%s M to $%s M' % (round(pricequintiles[2]/1000000, 2), round(pricequintiles[3]/1000000, 2))
    l5 = '> $%s M' % str(round(pricequintiles[3]/1000000, 2))

    # Plot scatter based on price quintiles
    ax.scatter(q1['Longitude'], q1['Latitude'], s=75, zorder = 2, c='darkred', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l1)    
    ax.scatter(q2['Longitude'], q2['Latitude'], s=75, zorder = 2, c='salmon', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l2)    
    ax.scatter(q3['Longitude'], q3['Latitude'], s=75, zorder = 2, c='grey', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l3)
    ax.scatter(q4['Longitude'], q4['Latitude'], s=75, zorder = 2, c='cornflowerblue', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l4)    
    ax.scatter(q5['Longitude'], q5['Latitude'], s=75, zorder = 2, c='darkblue', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l5)    

    # Add text box to map
    lgnd = ax.legend(loc = 2, prop = {'size': 25}, title = r'$\bf{San\/Francisco\/\/}$', title_fontsize=30)
    
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
    q1 = data.loc[data['Price'] < pricequintiles[0]]
    q2 = data.loc[(data['Price'] > pricequintiles[0]) & (data['Price'] < pricequintiles[1])]
    q3 = data.loc[(data['Price'] > pricequintiles[1]) & (data['Price'] < pricequintiles[2])]
    q4 = data.loc[(data['Price'] > pricequintiles[2]) & (data['Price'] < pricequintiles[3])]
    q5 = data.loc[data['Price'] > pricequintiles[3]]

    # Create legend labels
    l1 = '< $%s M' % str(round(pricequintiles[0]/1000000, 1))
    l2 = '\$%s M to $%s M' % (round(pricequintiles[0]/1000000, 1), round(pricequintiles[1]/1000000, 1))
    l3 = '\$%s M to $%s M' % (round(pricequintiles[1]/1000000, 1), round(pricequintiles[2]/1000000, 1))
    l4 = '\$%s M to $%s M' % (round(pricequintiles[2]/1000000, 1), round(pricequintiles[3]/1000000, 1))
    l5 = '> $%s M' % str(round(pricequintiles[3]/1000000, 1))

    # Plot scatter based on price quintiles
    ax.scatter(q1['Longitude'], q1['Latitude'], s=75, zorder = 2, c='darkred', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l1)    
    ax.scatter(q2['Longitude'], q2['Latitude'], s=75, zorder = 2, c='salmon', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l2)    
    ax.scatter(q3['Longitude'], q3['Latitude'], s=75, zorder = 2, c='grey', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l3)
    ax.scatter(q4['Longitude'], q4['Latitude'], s=75, zorder = 2, c='cornflowerblue', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l4)    
    ax.scatter(q5['Longitude'], q5['Latitude'], s=75, zorder = 2, c='darkblue', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l5)    

    # Add text box to map
    lgnd = ax.legend(loc = 4, prop = {'size': 25}, title = r'$\bf{East\/Bay\/\/}$', title_fontsize=30)
    
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
    q1 = data.loc[data['Price'] < pricequintiles[0]]
    q2 = data.loc[(data['Price'] > pricequintiles[0]) & (data['Price'] < pricequintiles[1])]
    q3 = data.loc[(data['Price'] > pricequintiles[1]) & (data['Price'] < pricequintiles[2])]
    q4 = data.loc[(data['Price'] > pricequintiles[2]) & (data['Price'] < pricequintiles[3])]
    q5 = data.loc[data['Price'] > pricequintiles[3]]

    # Create legend labels
    l1 = '< $%s M' % str(round(pricequintiles[0]/1000000, 1))
    l2 = '\$%s M to $%s M' % (round(pricequintiles[0]/1000000, 1), round(pricequintiles[1]/1000000, 1))
    l3 = '\$%s M to $%s M' % (round(pricequintiles[1]/1000000, 1), round(pricequintiles[2]/1000000, 1))
    l4 = '\$%s M to $%s M' % (round(pricequintiles[2]/1000000, 1), round(pricequintiles[3]/1000000, 1))
    l5 = '> $%s M' % str(round(pricequintiles[3]/1000000, 1))

    # Plot scatter based on price quintiles
    ax.scatter(q1['Longitude'], q1['Latitude'], s=75, zorder = 2, c='darkred', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l1)    
    ax.scatter(q2['Longitude'], q2['Latitude'], s=75, zorder = 2, c='salmon', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l2)    
    ax.scatter(q3['Longitude'], q3['Latitude'], s=75, zorder = 2, c='grey', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l3)
    ax.scatter(q4['Longitude'], q4['Latitude'], s=75, zorder = 2, c='cornflowerblue', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l4)    
    ax.scatter(q5['Longitude'], q5['Latitude'], s=75, zorder = 2, c='darkblue', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l5)    

    # Add text box to map
    lgnd = ax.legend(loc = 3, prop = {'size': 25}, title = r'$\bf{Peninsula\/\/}$', title_fontsize=30)
    
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
    q1 = data.loc[data['Price'] < pricequintiles[0]]
    q2 = data.loc[(data['Price'] > pricequintiles[0]) & (data['Price'] < pricequintiles[1])]
    q3 = data.loc[(data['Price'] > pricequintiles[1]) & (data['Price'] < pricequintiles[2])]
    q4 = data.loc[(data['Price'] > pricequintiles[2]) & (data['Price'] < pricequintiles[3])]
    q5 = data.loc[data['Price'] > pricequintiles[3]]

    # Create legend labels
    l1 = '< $%s M' % str(round(pricequintiles[0]/1000000, 1))
    l2 = '\$%s M to $%s M' % (round(pricequintiles[0]/1000000, 1), round(pricequintiles[1]/1000000, 1))
    l3 = '\$%s M to $%s M' % (round(pricequintiles[1]/1000000, 1), round(pricequintiles[2]/1000000, 1))
    l4 = '\$%s M to $%s M' % (round(pricequintiles[2]/1000000, 1), round(pricequintiles[3]/1000000, 1))
    l5 = '> $%s M' % str(round(pricequintiles[3]/1000000, 1))

    # Plot scatter based on price quintiles
    ax.scatter(q1['Longitude'], q1['Latitude'], s=75, zorder = 2, c='darkred', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l1)    
    ax.scatter(q2['Longitude'], q2['Latitude'], s=75, zorder = 2, c='salmon', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l2)    
    ax.scatter(q3['Longitude'], q3['Latitude'], s=75, zorder = 2, c='grey', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l3)
    ax.scatter(q4['Longitude'], q4['Latitude'], s=75, zorder = 2, c='cornflowerblue', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l4)    
    ax.scatter(q5['Longitude'], q5['Latitude'], s=75, zorder = 2, c='darkblue', edgecolors = 'black', transform=ccrs.PlateCarree(), label = l5)    

    # Add text box to map
    lgnd = ax.legend(loc = 3, prop = {'size': 25}, title = r'$\bf{South\/Bay\/\/}$', title_fontsize=30)
    
    #change the marker size manually for both lines
    lgnd.legendHandles[0]._sizes = [150]
    lgnd.legendHandles[1]._sizes = [150]
    lgnd.legendHandles[2]._sizes = [150]
    lgnd.legendHandles[3]._sizes = [150]
    lgnd.legendHandles[4]._sizes = [150]
    
    plt.show()
    
    
    
    
# Scatter plot of color-coded prices across the bay
def cartoplot_commute(mapsize, shapefile, data):
        
    # Create a Stamen terrain background instance
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (mapsize,mapsize))
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    
    # Set range of map, stipulate zoom level
    ax.set_extent([-122.7, -121.5, 37.15, 38.15], crs=ccrs.Geodetic())
    ax.add_image(stamen_terrain, 12, zorder = 0)
        
    # color zipcodes by commute time
    from matplotlib import cm
    import matplotlib.colors
    cmap = cm.get_cmap('seismic', 100)
    norm = matplotlib.colors.Normalize(vmin = min(data['Min commute']), 
                                       vmax = max(data['Min commute']))
    color = cmap(norm(data['Min commute'].values))
    
    # add colorbar    
    n_cmap = cm.ScalarMappable(norm=norm, cmap='seismic')
    n_cmap.set_array([])
    cax = fig.add_axes([0.2, 0.15, 0.02, 0.25])
    cbar = ax.get_figure().colorbar(n_cmap, cax)
    
    # set colorbar label, properties
    cbar.set_label('Commute\ntime\n(minutes)', rotation = 0, labelpad = 15, y = 0.615, ha = 'left')    
    cbar.ax.tick_params(labelsize = 16)
    cax.yaxis.set_ticks_position('left')
    text = cax.yaxis.label
    font = matplotlib.font_manager.FontProperties(family = 'Helvetica', size = 20)
    text.set_font_properties(font)
    for tick in cbar.ax.yaxis.get_ticklabels():
        tick.set_family('Helvetica')    
    
    # add shapefile features
    shape_feature = ShapelyFeature(Reader(shapefile).geometries(), ccrs.epsg(26910), linewidth = 2)
    
    # Add commute data by zip code
    for counter, geom in enumerate(shape_feature.geometries()):
        if data['Area'][counter] < 50:
            if data['Population'][counter] > 500:
                ax.add_geometries([geom], crs=shape_feature.crs, 
                              facecolor=color[counter], edgecolor='k', alpha=0.8)
        else:
            continue
    # save figure, show figure
    fig = plt.gcf()
    plt.savefig('commute_plot.jpg', bbox_inches = 'tight', dpi = 600)
    plt.show()



# Scatter plot of color-coded prices across the bay
def cartoplot_schools(mapsize, shapefile, data):
        
    # Create a Stamen terrain background instance
    stamen_terrain = cimgt.Stamen('terrain-background')
    fig = plt.figure(figsize = (mapsize,mapsize))
    ax = fig.add_subplot(1, 1, 1, projection=stamen_terrain.crs)
    
    # Set range of map, stipulate zoom level
    ax.set_extent([-122.7, -121.5, 37.15, 38.15], crs=ccrs.Geodetic())
    ax.add_image(stamen_terrain, 12, zorder = 0)
        
    # set up colormap
    from matplotlib import cm
    import matplotlib.colors
    cmap = cm.get_cmap('seismic_r', 100)
    norm = matplotlib.colors.Normalize(vmin = min(data['School score']), 
                                       vmax = max(data['School score']))    
    color = cmap(norm(data['School score'].values))
    
    # add colorbar    
    n_cmap = cm.ScalarMappable(norm=norm, cmap='seismic_r')
    n_cmap.set_array([])
    cax = fig.add_axes([0.185, 0.15, 0.02, 0.25])
    cbar = ax.get_figure().colorbar(n_cmap, cax)
    
    # set colorbar label, properties
    cbar.set_label('School score\n(% proficient)', rotation = 0, labelpad = 15, y = 0.55, ha = 'left')    
    cbar.ax.tick_params(labelsize = 16)
    cax.yaxis.set_ticks_position('left')
    text = cax.yaxis.label
    font = matplotlib.font_manager.FontProperties(family = 'Helvetica', size = 20)
    text.set_font_properties(font)
    for tick in cbar.ax.yaxis.get_ticklabels():
        tick.set_family('Helvetica')    

    # add shapefile features
    shape_feature = ShapelyFeature(Reader(shapefile).geometries(), ccrs.epsg(26910), linewidth = 2)
    
    # Add commute data by zip code
    for counter, geom in enumerate(shape_feature.geometries()):
        if data['Area'][counter] < 50:
            if data['Population'][counter] > 500:
                ax.add_geometries([geom], crs=shape_feature.crs, 
                              facecolor=color[counter], edgecolor='k', alpha=0.8)
        else:
            continue
    
    # save figure, show figure
    fig = plt.gcf()
    plt.savefig('schools_plot.jpg', bbox_inches = 'tight', dpi = 600)
    plt.show()
