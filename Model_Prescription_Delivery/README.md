Things to be careful for:
- When you go to use the shortest path algorithm in the graphical modeler, ensure that the coordinate you copied is in WGS84. The shortest path algorithm in the graphical modeler uses EPSG:3857. 
- The shortest path algorithm will not calculate the distance from itself to itself so be wary of this if you code anything later. 
