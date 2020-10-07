#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: omarkawach
"""
# Import packages
import geopandas as gpd
import numpy as np
from shapely.geometry import Point

# Load data
neighbourhoods = gpd.read_file("../shapefiles/DAs_with_OD_Matrix/DAs_with_OD_Matrix.shp")

# We'll delete any costs above 2500m 
for index, row in neighbourhoods.iterrows():
    if(row.OD_total_c > 2500):
       neighbourhoods.drop(index, inplace=True)
       
# New geodataframe that'll be exported as a shapefile
new_data = gpd.GeoDataFrame(columns=neighbourhoods.columns)


# Find DAs closest hospital
for index, row in neighbourhoods.iterrows():
    dauid = row.DAUID
    data = neighbourhoods.loc[neighbourhoods['DAUID'] == dauid]
    closest_hospital = data.loc[data['OD_total_c'].idxmin(), 'OD_destina']
    # Append to data frame
    new_data = new_data.append(data.loc[data['OD_destina'] == closest_hospital])

new_data = new_data.drop_duplicates()

new_data.to_file("../shapefiles/closest_hospitals/closest_hospitals.shp")


