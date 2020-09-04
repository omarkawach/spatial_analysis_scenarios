#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 12:16:25 2020

@author: omarkawach
"""

import matplotlib.pyplot as plt

import peartree as pt

path = '../shapefiles/OC_TRANSPO_ROUTES/OC_TRANSPO_ROUTES.shp'

# Automatically identify the busiest day and
# read that in as a Partidge feed
feed = pt.get_representative_feed(path)

# Set a target time period to
# use to summarize impedance
start = 7*60*60  # 7:00 AM
end = 10*60*60  # 10:00 AM

# Converts feed subset into a directed
# network multigraph
G = pt.load_feed_as_graph(feed, start, end)

fig, ax = pt.generate_plot(G)