#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: omarkawach
"""
# Import packages
import geopandas as gpd

# Load data
buildings = gpd.read_file("../shapefiles/healthcare_study_area/Buildings/buildings.shp")
cheo = gpd.read_file("../shapefiles/healthcare_study_area/cheo/cheo.shp")
general = gpd.read_file("../shapefiles/healthcare_study_area/General/general.shp")
rehab = gpd.read_file("../shapefiles/healthcare_study_area/Rehab/rehab.shp")

# Add new columns to geodataframe
buildings["CLOSE_HOSP"] = None
buildings["HOSP_DIST"] = None


# Iterate through the buildings to find it's closest hospital
for index in range(len(buildings)):

    # Closest hospital is empty
    closest_h = None
    
    # Current building
    building = buildings.loc[index]
    
    # We're indexing this way incase the ordering got messed up between the shapefiles
    cheo_hospital = cheo[cheo.Build_ID == building.Build_ID]
    general_hospital = general[general.Build_ID == building.Build_ID]
    rehab_center = rehab[rehab.Build_ID == building.Build_ID]
    
    # Distance from building to these hospitals
    # List of distances
    list_of_dist = [cheo_hospital.cost[index], general_hospital.cost[index], rehab_center.cost[index]]
    closest_dist = min(list_of_dist)
    
    # See which hospital is closest
    if(closest_dist == list_of_dist[0]):
        closest_h = 'cheo'
    elif(closest_dist == list_of_dist[1]):
        closest_h = 'general'
    else:
        closest_h = 'rehab'
    
    # Save the data to the neighbourhoods geodataframe
    buildings.loc[index, 'CLOSE_HOSP'] = closest_h
    buildings.loc[index, 'HOSP_DIST'] = round(closest_dist/1000, 2)

# Save to shp
buildings.to_file("../shapefiles/healthcare_study_area/closest/closest.shp")