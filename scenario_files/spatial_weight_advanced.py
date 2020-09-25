#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: omarkawach
"""

# Import packages
from pysal.lib import weights
from pysal.lib import cg as geometry
import geopandas as gpd
import seaborn
import pandas 
import numpy
import matplotlib.pyplot as plt
from shapely.geometry import Polygon

# Load data
ottawa_da = gpd.read_file('../shapefiles/OttawaDA/OttawaDA.shp').to_crs(epsg=3857)

# Solve neighbour relations
# Disconnected observations (no neigbours) means there are polygons that
# dont share vertices with other polygons
wq = weights.contiguity.Queen.from_dataframe(ottawa_da) 
print(wq.n) # of spatial units
print(wq.s0) # number of joins
print(wq.pct_nonzero) # percent of nonzero weights (measure of density)
# This works out to 100 x (wq.s0 / wq.n^2)

'''
# Visualize adjacency relationships
ax = ottawa_da.plot(edgecolor='k', facecolor='w')
wq.plot(ottawa_da, ax=ax, 
        edge_kws=dict(color='r', linestyle=':', linewidth=1),
        node_kws=dict(marker=''))
ax.set_axis_off()
'''

# At zero, we can see we don't have disconnected observations
s = pandas.Series(wq.cardinalities)
s.plot.hist(bins=s.unique().shape[0]);

# Rook contiguity ignores common vertices
adjlist = wq.to_adjlist()
adjlist.head()

