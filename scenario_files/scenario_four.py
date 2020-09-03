#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: omarkawach
"""

# Here we depict the spatial weights network (planar)
# We can see that all neighbours are connected
import geopandas as gpd
from libpysal.weights.contiguity import Queen
from splot.libpysal import plot_spatial_weights

neighbourhoods = gpd.read_file("../shapefiles/ONS/ons.shp").to_crs(epsg=3857)
neighbourhoods.head()

weights = Queen.from_dataframe(neighbourhoods)

plot_spatial_weights(weights, neighbourhoods)