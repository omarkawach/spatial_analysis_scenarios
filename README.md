# Spatial Analysis Scenarios

### Overview

This repository explores various open sources tools one could use for performing geospatial analysis. The goal is to discuss a bank of simulation models that could be incorporated into [DEVS GIS Simulation Explorer](https://github.com/staubibr/arslab-web/tree/master/app-gis). There are interactive **Jupyter Notebooks** available for demo purposes via **Binder**. Developers can also install Python packages themselves and run the code on their own in **Spyder**. 

### Introduction

Large and small scale problems are difficult for humans to conceptualize. This is especially true when we consider global issues ([Resnik et al., 2016](https://onlinelibrary.wiley.com/doi/full/10.1111/cogs.12388)). The COVID-19 pandemic is one of the many global issues humanity has come to face in the 21st century. Local, national, and global real-time, non-real-time, or simulated disease cases must be carefully analyzed to address this challenge. Geographical tracking and mapping of the pandemic through the application of Geographic Information Systems (GIS) has been proven to be a powerful system for disease monitoring and planning ([Buolos & Geraghty, 2020](https://ij-healthgeographics.biomedcentral.com/articles/10.1186/s12942-020-00202-8)). Such a system has allowed researchers to present large volumes of data in an intuitive way. For one, web-based mapping has created an environment for accessible remote collaboration between decision makers ([Franch-Pardo et al., 2020](https://www.sciencedirect.com/science/article/pii/S0048969720335531)). By integrating simulation models into map-based web applications, researchers can also highlight spatiotemporal trends in various scenarios. This study aims to ...

### Background

GIS

[Spatial analysis](https://mgimond.github.io/Spatial/introGIS.html)

Visualization

### Things to Discuss

Example scenarios will fall into one or more of the following categories:
- Spatial Join (analysis)
  - [Spatial relationship types](https://desktop.arcgis.com/en/arcmap/latest/extensions/data-reviewer/types-of-spatial-relationships-that-can-be-validated.htm)
    - Touches
    - Contains
    - Intersects
    - Relation
    - Within
    - Crosses
    - Overlaps

- Topological
  - A topology is...to be cont'd
  - Buffers
  - [Voronoi diagrams embody a form of "automated" topology](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.86.3356&rep=rep1&type=pdf)
  - Spatial networks 
    - [Planar if 2D and edges only intersecting at the nodes ](https://arxiv.org/pdf/1611.01890.pdf)
- Geostatistical 
  - Geostatistics is...to be cont'd
  - [First law of geography](https://wiki.gis.com/wiki/index.php/First_law_of_geography) 
- Attribute Query
  - Attribute queries are...to be cont'd
- Proximity Analysis
  - Something...
- Network Analysis
  - Roads, busses, etc...to be cont'd

## Demo Notebook Scenarios

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/omarkawach/spatial_analysis_scenarios.git/master)

Steps:
- Click the icon above to launch this repository in Jupyter Notebook
- Once Binder loads the repo in Jupyter Notebook, Select the `scenario_notebooks` folder
- Select any notebook to demo
- Set kernel to Python 3
- Click `Run` to move down one cell
  - Keep clicking `Run` to move down another cell

**Note:** Some cells may need more than a few seconds or minutes to run. 

## Development Setup
1. In a console, cd into your desired directory and run the following:
   
   `git clone https://github.com/omarkawach/spatial_analysis_scenarios.git`
   
2. [Download Anaconda and then launch Spyder](https://www.anaconda.com/products/individual)
   

3. Open a console where you cloned the repo, install all necessary python packages in one go using:
   
   ` pip install --use-feature=2020-resolver -r packages.txt `

4. You may now run/manipulate code

## Models

### Emergency Assistance - Health Unit Services 



## Scenarios

See [Appendix](https://github.com/omarkawach/spatial_analysis_scenarios#appendix) for details on files, packages, and data sources used. 

### Healthcare - Finding Polygons that Contain Hospitals

Ottawa resident, Mary, is looking for a new apartment to rent. She tells her Real Estate Agent that she would like to live within a boundary that has a hospital in it since she requires regular visits for post-op checkups. To meet Mary's apartment critieria, a spatial join (analysis) must be conducted. 

GIS analysts conduct spatial joins by taking one feature and seeing if it *intersects* with another feature. In this case, the GIS analyst would see if a hospital point is within an ONS polygon. This would allow us to define new neighbourhoods based on whether a polygon has a hospital or not. For this spatial join, we could also try one or more spatial relationship types like *touches, contains, within,* and *relation*. 

After analysis, Mary would receive results stating that she may look for apartments in the ten following areas: 
- Civic Hospital
- Central Park
- Billings Bridge 
- Alta Vista
- Riverview
- Wateridge Village
- Qualicum 
- Redwood Park
- West Centretown
- Byward Market


![](scenario_images/polygons_with_hospitals/result.png)

**Figure 1**. ONS polygons with Hospitals in them




### Healthcare - Voronoi Diagrams for Hospital Proximity Study

If you were a resident around Central Ottawa, you'd likely want to know which hospital(s) you could get to fastest in the event of an emergency. Proxomity analysis through Voronoi diagrams allows analysts to find the closest point within a region. For this scenario, we have a large number of ONS polygons and 10 hospitals (point data). The Voronoi regions are built using the hospitals and then intersected with ONS polygons to identify which neighbourhoods are closest to a hospital. 

![](scenario_images/voronoi_hospitals/qgis.png)

**Figure 2**. ONS Closest to Hospitals

![](scenario_images/voronoi_hospitals/table.png)

**Figure 3**. Peview of Attribute Table for Figure 2

### Healthcare - Assign Hospitals to Ottawa DAs for Ambulance Dispatching

9-11 Operators are looking for more efficient ways to help those in need. Through proximity analysis, researchers can discover the closest hospital to a caller's DA. This would allow ambulances to be dispatched accordingly. The analysis first begins by building a topology where we address ONS polygons within 5km of a hospital. Once we have our desired ONS polygons, the centroid of each polygon is extracted. The centroid from each polygon will be used to calculate the distance from the centroid to a hospital. The closest hospital to a polygon's centroid will be used for assigning hospitals to polygons. This would conclude our proximity analysis. 



![](scenario_images/hospitals_to_polygons/qgis.png)

**Figure 4**. Ottawa DAs Intersecting with 5km Hospital Buffer (Dissolved)

**Legend**

<img src="scenario_images/hospitals_to_polygons/legend.png" alt="legend_two" width="400" height="280" />

![](scenario_images/hospitals_to_polygons/python.png)

**Figure 5**. Ottawa DAs with the Closest Hospital 



### Healthcare - Dispatching Ambulances using Ottawa Road Network

Through topological studies and proximity analysis, 9-11 Operators discovered what hospital each ONS polygon should be assigned. Now, it's time for them to put their research to the test. 9-11 Operators just received a call from someone living in the Royal Ottawa Hospital neighbourhood. In order to get an ambulance to the caller's building quickly, they require network analysis. The shortest path algorithm is run on Ottawa's Road Network from the hospital to the caller's building. 

![](scenario_images/hospitals_to_polygons_advanced/hospitals_label.png)

**Figure 6**. Location of Hospitals in Ottawa

**Legend**

<img src="scenario_images/hospitals_to_polygons_advanced/legend.png" alt="legend_two" width="210" height="200" />

![](scenario_images/hospitals_to_polygons_advanced/qgis.png)

**Figure 7**. Ottawa DAs Mapped to their Nearest Hospital

![](scenario_images/hospitals_to_polygons_advanced/shortest_path.png)

**Figure 8**. Shortest Path from Hospital to Caller's Home

*Possible Use Case*
1. During a pandemic, we don't want to overwhelm hospitals. 
   - Only allow patients into a hospital if they're from a specific ONS polygon
      - Number of accepted ONS polygons for a hospital could be based on population, number of buildings, etc.

Come up with resulting model 

Any house that emits a call

### Disaster Response - Chemical Spill at Hospital

Ottawa's Montfort Hospital has had a chemical spill. Residents who are directly within 1km of the hospital are warned to evacuate immediately. Residents whose ONS Boundary *intersect* with the 1km buffer are also expected to evacuated moments later. Before First Responders head into the polygons impacted by the chemical spill, they want to know how many buildings are impacted so that they may act by prioirity. This research would allow First Responders to know an approximate headcount as well. 

![](scenario_images/chemical_spill/qgis.png)

**Figure 9**. Overview of Chemical Spill Scenario

<img src="scenario_images/chemical_spill/immediate_impact.png" alt="result_seven_within_buffer" width="400" height="50" />

**Figure 10**. Number of Buildings Directly Impacted within 1km Buffer

<img src="scenario_images/chemical_spill/neighbourhoods_impacted.png" alt="result_seven_within_boundaries" width="400" height="300" />

**Figure 11**. Number of Buildings Impacted by ONS Polygon


*Possible Use Cases*
1. Go further and evacuate neighbourhoods that are touching impacted neighbourhoods. 
2. Be better prepared for potential future events like the [Lac-Mégantic rail disaster](https://www.tsb.gc.ca/eng/rapports-reports/rail/2013/r13d0054/r13d0054-r-es.html)
   - Help dispatch and evacuate people. 
3. Unrelated to emergencies, we could see which buildings are in a DA and connect them for population growth analysis.

### Disaster Response - Power Generator Outage after Tornado

A recent tornado has resulted in a power outage to all Ottawa DAs within 10km of the Rideau Falls Energy Station. The City of Ottawa would like to know the number of buildings and Ottawa DAs impacted. This can be done by assigning each building to the correct DA. 

![](scenario_images/power_outage/qgis.png)

**Figure 12**. Ottawa DAs and Buildings Without Power

```
Buildings without power: 88,780
Total Ottawa DAs impacted: 592
```


### Dealing with Populations - Classify Neighbourhoods by Population Density

At Statistics Canada, an intern would like to conduct a population density study using ONS data. The data gathered would be used for defining new neighbourhoods based on a simple quartile classification algorithm. 


![](scenario_images/ONS_population_density/density.png)

**Figure 13**. ONS Population Density

**Legend**

<img src="scenario_images/ONS_population_density/legend.png" alt="legend_five" width="200" height="120" />

<img src="scenario_images/ONS_population_density/quartile.png" alt="result_five"
 width="370" height="250" />

**Figure 14**. ONS Quartile Classification for New Neighbourhoods

*Potential Use Case*
1. Model highly infectious populations according to population density
   - We may theorize that more dense areas play an impact on the number of cases in neighbouring polygons. 
   - Expand to have topological relationships 
     - Maybe have buffers based on infection spread

### Delivery - Pharmacy Prescription Delivery

Prescription drugs are now available for delivery to customers. A Canadian pharmacy chain, Shoppers Drug Mart, finds that one of their customers lives near 3 Shoppers locations. To decide which store should send a driver to deliver the medication, they use QGIS' shortest path algorithm from the network analysis toolbar. The shortest path cost will be calculated in meters. Default speed is 50km/hr.

![](scenario_images/shoppers_drug_mart/qgis.png)

**Figure 15**. Shortest Path from Iverness / Benson to Nearest Shoppers

![](scenario_images/shoppers_drug_mart/table.png)

**Figure 16**. Table of Shortest Path for Figure 15

### Transit - Finding the Nearest Bus Stop(s) to a Building 

Find the nearest bus stop to each building within specific Ottawa DAs. This can be done by using bus stops to create voronoi polygons. Then, intersect the voronoi polygons with the Ottawa DAs. This scenario assumes that the vertices from each bus route are bus stops, even if that is not the case.  

![](scenario_images/voronoi_bus_stops/qgis.png)

**Figure 17**. Overview of Closest Bus Stop(s) to each Building in DAs

### Travel - Fastest Route to the First Road Crossing in a List

We're in the center of Ottawa and want to find the shortest path to a road crossing through network analysis. 

![](scenario_images/shortest_path_road_crossing/python.png)

**Figure 18**. Shortest path

*Potential Use Case*
1. Find shortest path from warehouse to multiple stores 
2. Link distribution centers to population centers


### Spatial Weights - Proximity Analysis between Polygons

*Category*
- Topology
- Spatial Statistics 

For the ONS dataset, we are looking for ways to represent the spatial relationships between polygons. We do this by depicting a spatial weight network (planar). In this case, the Queen contiguity weight lets us look at shared edges or vertices between polygons. 

<img src="scenario_images/ONS_spatial_weight/python.png" alt="result_four" width="300" height="220" />

**Figure 19**. Spatial Weight Network Ottawa

*Potential Use Case*
1. [Boundary Detection](https://geographicdata.science/book/notebooks/04_spatial_weights.html) to observe differences in wealth (Spatial Econometrics)
   - [Combining spatial statistics and spatial data analysis](http://resources.esri.com/help/9.3/arcgisengine/java/gp_toolref/spatial_statistics_toolbox/spatial_weights.htm)


## Credits and Acknowledgements

[Carleton University - ARSLab](https://arslab.sce.carleton.ca/) 

[Qiusheng Wu - Python Geospatial Repo on GitHub](https://github.com/giswqs/python-geospatial)

## Resources

### Notebooks

[Binder: ](https://mybinder.org/)Notebooks in an Executable Environment

[Jupyter Notebook: ](https://jupyter.org/)Interactive Python Notebooks

### Python Packages

[Matplotlib: ](https://matplotlib.org/)Visualization with Python

[Pandas: ](https://pandas.pydata.org)Data Analysis in Python

[GeoPandas: ](https://geopandas.org/)Work with Geospatial Data in Python

[Shapely: ](https://pypi.org/project/Shapely/)Manipulate and Analyze Geometric Objects

[NetworkX: ](https://networkx.github.io/)Network Analysis in Python

[OSMnx: ](https://github.com/gboeing/osmnx)Python for Street Networks

[PyProj: ](https://github.com/pyproj4/pyproj)For Projections in Geospatial Data

[PySal: ](https://pysal.org/)Spatial Analysis Library

[NumPy: ](https://numpy.org/)Scientific Computing with Python

[Descartes: ](https://pypi.org/project/descartes/)For Plotting Polygons in GeoPandas

[Geovoronoi:](https://github.com/WZBSocialScienceCenter/geovoronoi) For Plotting Voronoi Regions inside Geographic Regions

### Geospatial Analysis Program(s)

[QGIS Download: ](https://www.qgis.org/en/site/)Open Source Geospatial Analysis Program

[QGIS Docs](https://www.qgistutorials.com/en/): Tutorials and Tips

### IDE

[Spyder: ](https://www.spyder-ide.org/)Scientific Python Development Environment



## Appendix 

### Dataset Sources

**[Ottawa Neighbourhood Study (ONS) from Carleton University](https://library.carleton.ca/find/gis/geospatial-data/ottawa-neighbourhoods)**

*Shapefile Location*

See [`/shapefiles/ONS`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/ONS)


*Description from source:*
```
The ONS Neighbourhood Boundaries were created by the Ottawa Neighbourhood Study
(ONS) to analyse population statistics and are not indicative of actual 
neighbourhood limits.  Neighbourhood refers to an inhabited area delineated by 
social and physical boundaries. ONS neighbourhood boundaries were derived based on 
census tracts, physical and demographic similarities, physical barriers (e.g. 
waterways, highways, etc.), maps used by the real estate profession (e.g. the 
Ottawa Multiple Listing Service), consultations with community stakeholders, as 
well as fieldwork by ONS researchers.

108 neighbourhood boundaries are included in the shapefile, 
from Barrhaven to Woodvale. 
```

**[Hospitals from Open Ottawa](https://open.ottawa.ca/datasets/b769ce497f2540aa962e602c983994d6_0?geometry=-76.050%2C45.348%2C-75.396%2C45.433)**

*Shapefile Location*

See [`/shapefiles/OttawaHospitals`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/OttawaHospitals)

*Description from source:*
```
Map containing point features of Hospitals located in the City of Ottawa.
```

**[Open Database of Building from Statistics Canada](https://www.statcan.gc.ca/eng/lode/databases/odb)**

*Shapefile Location*

See [`/shapefiles/OttawaBuildings.zip`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/OttawaBuildings.zip)

*Description from source:*

```
The Open Database of Buildings (ODB) is a collection of open data on buildings,
primarily building footprints, and is made available under the Open Government 
License - Canada.
```

**[Ottawa Dissemination Areas (DA) from Open Ottawa](https://open.ottawa.ca/datasets/89fe8cb18d7345b2b666623ccb872310_0?geometry=-78.333%2C44.878%2C-73.101%2C45.555)**

*Shapefile Location*

See [`/shapefiles/OttawaDA`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/OttawaDA)

*Description from source:*

```
The Dissemination Area Boundary Files portray the dissemination area boundaries
for which Census data are disseminated. A dissemination area is a small area
composed of one or more neighbouring dissemination blocks and is the smallest
standard geographic area for which all census data are disseminated.
```

**[OC Transpo Routes from Carleton University](https://library.carleton.ca/find/gis/geospatial-data/oc-transpo-transit-routes)**

*Shapefile Location*

See [`/shapefiles/OC_TRANSPO_ROUTES`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/OC_TRANSPO_ROUTES)

*Modifications to Original Dataset in this Repo:*

The dataset came with hundreds of shapefiles. All the shapefiles were merged into one. 

*Description from source:*

```
Individual vector transit routes for OC Transpo between 1929 and 2015. 

The following information was collected for each transit route:
- Route Number
- Route Type (Regular, Peak, Express, Rural, etc.)
- Mode of Transportation (bus, train)
- Year
```


**[Road Network Files from Statistics Canada](https://www12.statcan.gc.ca/census-recensement/2011/geo/RNF-FRR/index-eng.cfm)**

*Shapefile Location*

See [`/shapefiles/OttawaRoads`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/OttawaRoads)

*Modifications to Original Dataset in this Repo:*

The dataset came with the whole road network of Canada. Modified the dataset to only have Ottawa's road network. 

*Description from source:*

```
Road network files are digital representations of Canada's
national road network, containing information such as street
names, types, directions and address ranges.
```
### Scenario Files and Packages

##### Healthcare - Finding Polygons that Contain Hospitals

*Files Used*
- [Python Script](https://github.com/omarkawach/spatial_analysis_scenarios/blob/master/scenario_files/polygons_with_hospitals.py) or [Notebook](https://github.com/omarkawach/spatial_analysis_scenarios/blob/master/scenario_notebooks/polygons_with_hospitals.ipynb)
- Shapefile from [`spatial_analysis_scenarios/shapefiles/ONS`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/ONS)
- Shapefile from [`spatial_analysis_scenarios/shapefiles/OttawaHospitals`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/OttawaHospitals)

*Python Packages Used*
- GeoPandas to read shapefiles
- Matplotlib to plot data

##### Healthcare - Voronoi Diagrams for Hospital Proximity Study

*Files Used*
- Shapefile from [`spatial_analysis_scenarios/shapefiles/ONS`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/ONS)
- Shapefile from [`spatial_analysis_scenarios/shapefiles/OttawaHospitals`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/OttawaHospitals)

##### Healthcare - Assign Hospitals to Ottawa DAs for Ambulance Dispatching

*Files Used*
- [Python Script](https://github.com/omarkawach/spatial_analysis_scenarios/blob/master/scenario_files/hospitals_to_polygons.py) or [Notebook](https://github.com/omarkawach/spatial_analysis_scenarios/blob/master/scenario_notebooks/hospitals_to_polygons.ipynb)
- Shapefile from [`spatial_analysis_scenarios/shapefiles/OttawaDA_nearHospital`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/OttawaDA_nearHospital)
  - This was originally the shapefile from [`spatial_analysis_scenarios/shapefiles/OttawaDA`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/OttawaDA) but then it was modified in QGIS to only hold polygons that intersect within a 5km buffer of all the hospitals (see figure 4)
- Shapefile from [`spatial_analysis_scenarios/shapefiles/OttawaHospitals`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/OttawaHospitals)

*Python Packages Used*
  - GeoPandas to read shapefiles
  - Matplotlib to plot data
  - Shapely to create GeoSeries' for calculating distances 
  - PyProj to change the espg of shapefiles

##### Healthcare - Dispatching Ambulances using Ottawa Road Network

*Files Used*
- Shapefile created in [`spatial_analysis_scenarios/scenario_files/hospitals_to_polygons_advanced.py`](https://github.com/omarkawach/spatial_analysis_scenarios/blob/master/scenario_files/scenario_two_advanced.py) and saved to [`spatial_analysis_scenarios/shapefiles/HospitalsAndDAs`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/HospitalsAndDAs)
  - The original shapefile was from [`spatial_analysis_scenarios/shapefiles/OttawaDA`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/OttawaDA) but then it was modified in QGIS to only hold polygons that intersect within a 5km buffer of all the hospitals
- Shapefile from [`spatial_analysis_scenarios/shapefiles/OttawaHospitals`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/OttawaHospitals)
- Shapefile from [`spatial_analysis_scenarios/shapefiles/OttawaRoads`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/OttawaRoads)

*Python Packages Used*
  - GeoPandas to read shapefiles
  - Shapely to create GeoSeries' for calculating distances 
  - PyProj to change the espg of shapefiles

##### Disaster Response - Chemical Spill at Hospital

*Files Used*
- Shapefile from [`spatial_analysis_scenarios/shapefiles/ONS`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/ONS)
  - Based on the buffer intersection, the shapefile was modified into [`spatial_analysis_scenarios/shapefiles/Chemical_Spill_ONS`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/Chemical_Spill_ONS)
- Shapefile from [`spatial_analysis_scenarios/shapefiles/OttawaHospitals`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/ONS)
- Shapefile from [`spatial_analysis_scenarios/shapefiles/OttawaBuildings.zip`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/OttawaBuildings.zip)

*QGIS Plugin Used*
- MMQGIS Plugin is convenient for creating buffers

##### Disaster Response - Power Generator Outage after Tornado

*Files Used*
- Text file from [`spatial_analysis_scenarios/locations/RideauFallsHydro.txt`](https://github.com/omarkawach/spatial_analysis_scenarios/blob/master/locations/RideauFallsHydro.txt)
- Shapefile from [`spatial_analysis_scenarios/shapefiles/BuildingsOutage`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/BuildingsOutage) which is a modified version of [`spatial_analysis_scenarios/shapefiles/OttawaBuildings.zip`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/OttawaBuildings.zip)
- Shapefile from [`spatial_analysis_scenarios/shapefiles/HydroDAs`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/HydroDAs) which is a modified version of [`spatial_analysis_scenarios/shapefiles/OttawaDA`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/OttawaDA)

##### Dealing with Populations - Classify Neighbourhoods by Population Density

*Files Used*
- [Python Script](https://github.com/omarkawach/spatial_analysis_scenarios/blob/master/scenario_files/ONS_population_density.py) or [Notebook](https://github.com/omarkawach/spatial_analysis_scenarios/blob/master/scenario_notebooks/ONS_population_density.ipynb)
- Shapefile from [`spatial_analysis_scenarios/shapefiles/ONS`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/ONS)

*Python Packages Used*
- GeoPandas to read shapefiles
- Matplotlib to plot data
- NumPy to help with classification

##### Delivery - Pharmacy Prescription Delivery

*Files Used*
- Text file from [`spatial_analysis_scenarios/locations/ShoppersOttawa.txt`](https://github.com/omarkawach/spatial_analysis_scenarios/blob/master/locations/ShoppersOttawa.txt)
- Shapefile from [`spatial_analysis_scenarios/shapefiles/ShoppersCustomer`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/ShoppersCustomer) which is a modified version of [`spatial_analysis_scenarios/shapefiles/OttawaBuildings.zip`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/OttawaBuildings.zip)
- Shapefile from [`spatial_analysis_scenarios/shapefiles/OttawaRoads`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/OttawaRoads)

##### Transit - Finding the Nearest Bus Stop(s) to a Building 

*Files Used*
- Shapefile from [`spatial_analysis_scenarios/shapefiles/Four_DAUIDs`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/Four_DAUIDs) which is a modified version of [`spatial_analysis_scenarios/shapefiles/OttawaDA`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/OttawaDA)
- Shapefile from [`spatial_analysis_scenarios/shapefiles/OC_ROUTES_DAUID_VERTICES`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/OC_ROUTES_DAUID_VERTICES) which is a modified version of [`spatial_analysis_scenarios/shapefiles/OC_TRANSPO_ROUTES`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/OC_TRANSPO_ROUTES)

##### Travel - Fastest Route to the First Road Crossing in a List

*Python Packages Used*
  - GeoPandas: To create GeoDataFrames
  - PyProj: To change the espg of GeoDataFrames
  - Pandas: Convert dictionary to a Panda Series
  - OSMnx: For graphing and statistics
  - NetworkX: To calculate the shortest path

##### Spatial Weights - Proximity Analysis between Polygons

*Files used*
- [Python Script](https://github.com/omarkawach/spatial_analysis_scenarios/blob/master/scenario_files/ONS_spatial_weight.py) or [Notebook](https://github.com/omarkawach/spatial_analysis_scenarios/blob/master/scenario_notebooks/ONS_spatial_weight.ipynb)
- Shapefile from [`spatial_analysis_scenarios/shapefiles/ONS`](https://github.com/omarkawach/spatial_analysis_scenarios/tree/master/shapefiles/ONS)

*Python Packages used*
  - GeoPandas: To read shapefiles
  - PySal: To calculate and plot spatial weights