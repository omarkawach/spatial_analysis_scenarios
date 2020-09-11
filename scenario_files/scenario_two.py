#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: omarkawach
"""
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

neighbourhoods = gpd.read_file("../shapefiles/OttawaDA_nearHospital/DA_nearHospital.shp")
neighbourhoods.head()

hospitals = gpd.read_file("../shapefiles/OttawaHospitals/Hospitals.shp")
hospitals.head()

# Quick brute force approach. Not the most efficient code, but it gets the job done...
closest_hospitals = []

# Check each neighbourhood
for n in neighbourhoods.DAUID:
    closest = -1;
    close_h = ""
    
    nx = neighbourhoods[neighbourhoods.DAUID == n].to_crs(epsg=3857)
    
    n_lon = nx.geometry.centroid.x.iloc[0]
    n_lat = nx.geometry.centroid.y.iloc[0]
    
    nx = gpd.GeoSeries([Point(n_lon, n_lat)])
            
    # Check each hospital
    for h in hospitals.NAME:
        hx = hospitals[hospitals.NAME == h].to_crs(epsg=3857)
        
        h_lon = hx.geometry.centroid.x.iloc[0]
        h_lat = hx.geometry.centroid.y.iloc[0]
        
        hx = gpd.GeoSeries([Point(h_lon, h_lat)])
            
        dist = hx.distance(nx)
        
        if(closest <= 0 or dist[0] <= closest):
            closest = dist[0]
            closest_h = h
            
    closest_hospitals.append([n, closest_h, round(closest/1000, 2)])

# Color
h = {hospitals.NAME[0]: 'red',
     hospitals.NAME[1]: 'blue',
     hospitals.NAME[2]: 'black',
     hospitals.NAME[3]: 'orange',
     hospitals.NAME[4]: 'purple',
     hospitals.NAME[5]: 'brown',
     hospitals.NAME[6]: 'yellow',
     hospitals.NAME[7]: 'green',
     hospitals.NAME[8]: 'gray',
     hospitals.NAME[9]: 'pink'}

fig, ax = plt.subplots()
neighbourhoods.plot(ax=ax, facecolor='gray');
for ch in closest_hospitals:
    nx = neighbourhoods[neighbourhoods.DAUID == ch[0]]
    nx.plot(ax=ax, facecolor=h[ch[1]])
plt.tight_layout();

# Save to shp
# some_file.to_file("")
    