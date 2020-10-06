#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: omarkawach
"""
# This is similar to scenario_python_files/hospitals_to_polygons_advanced.py
# but we instead focus on visualization here

# Load packages
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# Load data
# Change neighbourhoods file here
neighbourhoods = gpd.read_file("../shapefiles/OttawaDA_nearHospital/DA_nearHospital.shp")
hospitals = gpd.read_file("../shapefiles/OttawaHospitals/Hospitals.shp")

# Quick brute force approach. Not the most efficient code, but it gets the job done...
# May take a few minutes to run
closest_hospitals = []

# Check each neighbourhood
for n in neighbourhoods.DAUID:
    # Set the closest distance to -1
    closest = -1;
    # Closest hospital is an empty string
    close_h = ""
    
    # Best to use this CRS when dealing with distance
    nx = neighbourhoods[neighbourhoods.DAUID == n].to_crs(epsg=3857)
    
    # Find the center of the polygon 
    n_lon = nx.geometry.centroid.x.iloc[0]
    n_lat = nx.geometry.centroid.y.iloc[0]
    
    # Save the coordinates into a GeoSeries
    nx = gpd.GeoSeries([Point(n_lon, n_lat)])
            
    # Check each hospital
    for h in hospitals.NAME:

        # Best to use this CRS when dealing with distance
        hx = hospitals[hospitals.NAME == h].to_crs(epsg=3857)
        
        # Find the center of the polygon 
        h_lon = hx.geometry.centroid.x.iloc[0]
        h_lat = hx.geometry.centroid.y.iloc[0]
        
        # Save the coordinates into a GeoSeries
        hx = gpd.GeoSeries([Point(h_lon, h_lat)])

        # Calculate the distance between the hospital and the neighbourhood     
        dist = hx.distance(nx) # Distance will be in meters
        
        # Find the closest distance
        if(closest <= 0 or dist[0] <= closest):
            closest = dist[0] # New closest distance
            closest_h = h # New closest hospital

    # Save the data [ONS polygon, closest hospital, distance in km]       
    closest_hospitals.append([n, closest_h, round(closest/1000, 2)])

h = {hospitals.NAME[0]: 'red', # Royal Ottawa Hospital
     hospitals.NAME[1]: 'blue', # Ottawa Hospital - Civic Campus
     hospitals.NAME[2]: 'black', # Ottawa Hospital - Riverside Campus
     hospitals.NAME[3]: 'orange', # CHEO
     hospitals.NAME[4]: 'purple', # Ottawa Hospital - General Campus
     hospitals.NAME[5]: 'brown', # Montfort Hospital
     hospitals.NAME[6]: 'yellow', # Queensway-Carleton Hospital
     hospitals.NAME[7]: 'green', # Rehab Center
     hospitals.NAME[8]: 'gray', # Saint Vincent Hospital
     hospitals.NAME[9]: 'pink'} # Elizabeth Bruyere Hospital

fig, ax = plt.subplots()
neighbourhoods.plot(ax=ax, facecolor='gray');
# Color the polygoons based on the hospital in them
for ch in closest_hospitals:
    nx = neighbourhoods[neighbourhoods.DAUID == ch[0]]
    nx.plot(ax=ax, facecolor=h[ch[1]])
plt.tight_layout();