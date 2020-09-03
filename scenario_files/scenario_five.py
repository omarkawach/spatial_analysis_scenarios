#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: omarkawach
"""
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt

neighbourhoods = gpd.read_file("../shapefiles/ONS/ons.shp")
neighbourhoods.head()

# Network spatial analysis using population
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
neighbourhoods.plot(ax=ax, facecolor='gray');

for index, row in gdf.iterrows():
    data = gdf.iloc[index]
    to_plot = gdf[gdf.Name == data.Name]
    if(data.POPEST <= quart[0]):
        to_plot.geometry.plot(ax=ax, facecolor=c['Q1'])
    elif(data.POPEST <= quart[1]):
        to_plot.plot(ax=ax, facecolor=c['Q2'])
    elif(data.POPEST <= quart[2]):
        to_plot.plot(ax=ax, facecolor=c['Q3'])
    else:
        to_plot.plot(ax=ax, facecolor=c['Q4'])
        
plt.tight_layout();