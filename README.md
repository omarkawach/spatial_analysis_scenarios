# Spatial Analysis Scenarios

Experimenting with GIS libraries and QGIS

## Installation

1. [Download Anaconda and then launch Spyder](https://www.anaconda.com/products/individual)
   

2. In a console, install all necessary python packages in one go
   * ` pip install --use-feature=2020-resolver -r requirements.txt `


## Tutorial

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/omarkawach/spatial_analysis_scenarios.git/master)

## Scenarios

#### First Scenario
Mary requires regular visits to the hospitals, and is looking for a new apartment to rent. 
Mary would like her apartment to be located in a neighbourhood with a hospital in it. 

![result](scenario_images/scenario_one.png)

**Figure 1**. 10 Neighbourhoods with Hospitals in them

#### Second Scenario
911 Operator Joseph needs to know which hospitals are closest to a caller's neighbourhood. 
Joseph will dispatch an ambulance from the nearest hospital.

**Legend**
![legend_two](scenario_images/scenario_two_legend.png)

![result_two](scenario_images/scenario_two.png)

**Figure 2**. Neighbourhoods with the closest hospital 

**NOTE**: The large blue region is Ottawa's greenbelt. It's center is far from Queensway-Carleton Hospital. 

#### Third Scenario
For some recent we're in the center of Ottawa and want to find the shortest path to a road crossing. 

![result_three](scenario_images/scenario_three.png)

**Figure 3**. Shortest path

#### Four Scenario
Perhaps for some weird QA purpose we wanted to check if all the neighbourhoods are connected. 
We could depict a spatial weight network (planar) to confirm things are in order. 

![result_four](scenario_images/scenario_four.png)

**Figure 4**. Spatial Weight Network Ottawa

#### Fifth Scenario
John is doing a study and population density in Ottawa's many neighbourhoods. 
He loads his shapefile and can now sort it to only hold geometry and population estimates. 

![result_five](scenario_images/scenario_fiv.png)

**Figure 4**. Population Density in Ottawa's Neighbourhoods

What John does with the data afterwards is up to him. 
For example, he could define new neighbourhoods based on certain classification algorithms.

**Legend**
![legend_five](scenario_images/scenario_five_leg.png)

![result_five_pop](scenario_images/scenario_five_pop_est.png)

**Figure 5**. Ottawa Neighbourhoods Quartile Classification

## Resources

#### Python Packages

[Matplotlib: Visualization with Python](https://matplotlib.org/)

[GeoPandas](https://geopandas.org/) 

[Shapely](https://pypi.org/project/Shapely/)

[NetworkX: Network Analysis in Python](https://networkx.github.io/)

[OSMnx: Python for Street Networks](https://github.com/gboeing/osmnx)

[PyProj](https://github.com/pyproj4/pyproj)

[PySal](https://pysal.org/)

[NumPy](https://numpy.org/)

#### Geospatial Analysis Program(s)

[QGIS](https://www.qgis.org/en/site/)

[QGIS Tutorials](https://www.qgistutorials.com/en/)

#### IDE

[Spyder: Scientific Python Development Environment](https://www.spyder-ide.org/)


