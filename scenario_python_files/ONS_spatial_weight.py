#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: omarkawach
"""
# Import packages
import geopandas as gpd
from libpysal.weights.contiguity import Queen
from splot.libpysal import plot_spatial_weights

# Load data
neighbourhoods = gpd.read_file("../shapefiles/ONS/ons.shp").to_crs(epsg=3857)

# Look at shared edges and vertices between polygons
weights = Queen.from_dataframe(neighbourhoods)

# Plot the spatial weighting 
plot_spatial_weights(weights, neighbourhoods)