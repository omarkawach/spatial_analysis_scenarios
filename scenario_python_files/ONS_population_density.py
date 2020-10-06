#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: omarkawach
"""
# Import packages
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt

# Load data
neighbourhoods = gpd.read_file("../shapefiles/ONS/ons.shp")


# Only grab the data we need
gdf = neighbourhoods[['geometry', 'POPEST', 'Name']]

gdf.plot(column = 'POPEST',
         cmap = 'OrRd', 
         figsize=(20,10),
         legend = True)

# Quartiles
quart = np.percentile(gdf.POPEST, [25, 50, 75])

# Color
c = {'Q1': 'white',
     'Q2': 'yellow',
     'Q3': 'orange',
     'Q4': 'red'}


fig, ax = plt.subplots()
# Plot our background (helps us to see boundary lines)
neighbourhoods.plot(ax=ax, facecolor='gray');
# Go through the dataframe
for index, row in gdf.iterrows():
    # Data holds geometry, popest, and name
    data = gdf.iloc[index]
    # to_plot holds the whole polygon 
    to_plot = gdf[gdf.Name == data.Name]
    # Now lets see what quartile the population fits into
    if(data.POPEST <= quart[0]):
        to_plot.geometry.plot(ax=ax, facecolor=c['Q1'])
    elif(data.POPEST <= quart[1]):
        to_plot.plot(ax=ax, facecolor=c['Q2'])
    elif(data.POPEST <= quart[2]):
        to_plot.plot(ax=ax, facecolor=c['Q3'])
    else:
        to_plot.plot(ax=ax, facecolor=c['Q4'])
plt.tight_layout();