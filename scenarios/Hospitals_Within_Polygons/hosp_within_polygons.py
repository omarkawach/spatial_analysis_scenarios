#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: omarkawach
"""
# Import packages
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
neighbourhoods = gpd.read_file("../../shapefiles/ONS/ons.shp")
hospitals = gpd.read_file("../../shapefiles/OttawaHospitals/Hospitals.shp")

# Plot data
fig, ax = plt.subplots()
# Make all the ONS polygons gray so that red highlighted polygons pop out more
neighbourhoods.plot(ax=ax, facecolor='gray');
# Go through each hospital by geometry
for h in hospitals.geometry:
    # Now go through each neighbourhood by name 
    # We have to intersect using nx or else the interpreter gets mad
    for n in neighbourhoods.Name:
        # Find the feature matching the name
        nx = neighbourhoods[neighbourhoods.Name == n]
        # See if the neighbourhood intersects with a hospital
        if(nx.geometry.intersects(h).any() == True):
            # If a neighbourhood has a hospital, color it's polygon red
            nx.plot(ax=ax, facecolor='red')
plt.tight_layout();