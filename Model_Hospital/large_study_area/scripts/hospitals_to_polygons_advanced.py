#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: omarkawach
"""
# Import packages
import geopandas as gpd
from shapely.geometry import Point

# Load data
neighbourhoods = gpd.read_file("../shapefiles/OttawaDA_nearHospital/DA_nearHospital.shp")
hospitals = gpd.read_file("../shapefiles/OttawaHospitals/Hospitals.shp")

# Quick brute force approach.
# Add new columns to geodataframe
neighbourhoods["CLOSEST_HOSPITAL"] = None
neighbourhoods["CH_DISTANCE"] = None
n_index = 0

# Check each neighbourhood (all 761)
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
        hx = hospitals[hospitals.NAME == h].to_crs(epsg=3857)
        
        h_lon = hx.geometry.centroid.x.iloc[0]
        h_lat = hx.geometry.centroid.y.iloc[0]
        
        hx = gpd.GeoSeries([Point(h_lon, h_lat)])
            
        # Calculate the distance between the hospital and the neighbourhood     
        dist = hx.distance(nx) # Distance will be in meters
        
        # Find the closest distance
        if(closest <= 0 or dist[0] <= closest):
            closest = dist[0] # New closest distance
            closest_h = h # New closest hospital
    
    # Save the data to the neighbourhoods geodataframe
    neighbourhoods.loc[n_index, 'CLOSEST_HOSPITAL'] = closest_h
    neighbourhoods.loc[n_index, 'CH_DISTANCE'] = round(closest/1000, 2)
    n_index += 1

# Save to shp
# neighbourhoods.to_file("../Model_Hospital/large_study_area/HospitalsAndDAs/Closest_H_to_DA.shp")

