#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: omarkawach
"""

import geopandas as gpd
from shapely.geometry import Point

neighbourhoods = gpd.read_file("../shapefiles/OttawaDA_nearHospital/DA_nearHospital.shp")
neighbourhoods.head()

hospitals = gpd.read_file("../shapefiles/OttawaHospitals/Hospitals.shp")
hospitals.head()

# Quick brute force approach. Not the most efficient code, but it gets the job done...
neighbourhoods["CLOSEST_HOSPITAL"] = None
neighbourhoods["CH_DISTANCE"] = None
n_index = 0
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
    
    neighbourhoods.loc[n_index, 'CLOSEST_HOSPITAL'] = closest_h
    neighbourhoods.loc[n_index, 'CH_DISTANCE'] = round(closest/1000, 2)
    n_index += 1

# Save to shp
neighbourhoods.to_file("/Users/omarkawach/Documents/QGIS/GIS_GIT/spatial_analysis_scenarios/shapefiles/HospitalsAndDAs/Closest_H_to_DA.shp")

