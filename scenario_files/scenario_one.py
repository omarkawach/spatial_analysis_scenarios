#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: omarkawach
"""
import geopandas as gpd
import matplotlib.pyplot as plt

neighbourhoods = gpd.read_file("../shapefiles/ONS/ons.shp")
neighbourhoods.head()

hospitals = gpd.read_file("../shapefiles/OttawaHospitals/Hospitals.shp")
hospitals.head()

fig, ax = plt.subplots()
neighbourhoods.plot(ax=ax, facecolor='gray');
for h in hospitals.geometry:
    for n in neighbourhoods.Name:
        nx = neighbourhoods[neighbourhoods.Name == n]
        if(nx.geometry.intersects(h).any() == True):
            nx.plot(ax=ax, facecolor='red')
plt.tight_layout();

# Save to shp
# neighbourhoods_and_hospitals.to_file("/Users/omarkawach/Documents/QGIS/Experimental/Ottawa/ONS/new_ons.shp")