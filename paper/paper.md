---
title: "Building-level Shortest Evacuation Time: A QGIS Plugin for Time-Based Evacuation Management"
tags:
  - QGIS
  - GIS
  - evacuation planning
  - disaster risk assessment
  - open-source
  - tsunami inundation
authors:
  - name: Gaurav Khairnar
    affiliation: 1
  - name: RS Mahendra
    affiliation: 1
  - name: Ch Patanjali
    affiliation: 1
  - name: TNC Kartik
    affiliation: 1
  - name: Sudheer Joseph
    affiliation: 1
  - name: TM Balakrishnan Nair
    affiliation: 1
affiliations:
  - name: Indian National Centre for Ocean Information Services, Ministry of Earth Sciences, Hyderabad
    index: 1
date: 2026-02-14
bibliography: paper.bib
---

# Summery
**Build Shortest Evacuation Time** is an open-source QGIS plugin that supports **building-level evacuation planning** for flood and inundation hazards. It automatically identifies buildings located within an inundation zone and computes **shortest evacuation routes** from those at-risk buildings to nearest safe shelters using Open Street Map (OSM) road network data. The plugin aims to assist GIS users and disaster risk planners in generating rapid evacuation path outputs with minimal input requirements

# Statement of need

Build Shortest Evacuation Time is an open-source QGIS plugin that supports building-level evacuation planning for flood and inundation hazards. The plugin automatically identifies buildings located within an inundation zone and computes shortest-time evacuation routes from at-risk buildings to the nearest safe shelters using OpenStreetMap (OSM) road network data. Unlike distance-based routing approaches, the tool estimates evacuation time and can optionally incorporate terrain slope from a Digital Elevation Model (DEM) to adjust walking speed. The plugin is designed to assist GIS users and disaster risk planners in generating rapid, reproducible, and terrain-aware evacuation analyses within an open-source GIS environment. 

**Build_Short_Evac_Time** a QGIS plugin addresses this gap by integrating inundation-based building selection with time-based network routing in a single interface. The theoretical framework of the tsunami walk-time modelling approach is described in Gaurav et al., (manuscript submitted and under review). This plugin provides an open-source implementation of that framework within QGIS, enabling reproducible and operational evacuation planning. The plugin computes evacuation time rather than only distance and assigns each building to the nearest shelter that can be reached in the shortest time. When a Digital Elevation Model (DEM) is provided, evacuation time can optionally be adjusted based on terrain slope along the evacuation route, allowing slope-dependent realistic walking speed estimation. The resulting evacuation time is stored as an attribute, and buildings can be classified according to evacuation time thresholds for further analysis and visualization. 

This tool supports disaster risk planners, researchers, and GIS practitioners in generating reproducible and terrain-aware evacuation analyses within an open-source GIS environment. 

# Functionality
The plugin operates within the QGIS environment and provides an integrated workflow for building-level evacuation time analysis. Its main functionality includes:

- **Input layers**:
  - Building footprints (vector layer in .shp or .geojson format)
  - Inundation or hazard extent polygon (vector layer in .shp or .geojson format)
  - Shelter locations (point layer in .shp or .geojson format)
  - Optional Digital Elevation Model (raster layer in preferably in .tiff format) for slope-based walking speed adjustment

- **At-risk building identification**:
  Buildings intersecting the inundation polygon are automatically detected and selected for evacuation analysis.

- **Time-based network routing**:
  For each at-risk building, the plugin computes evacuation routes to available shelters using the OSM road network. Evacuation time is calculated based on walking speed assumptions.

- **Minimum-time shelter allocation**:
  Each building is assigned to the shelter that can be reached in the shortest evacuation time rather than shortest distance.

- **Optional terrain-adjusted walking speed**:
  When a Digital Elevation Model (DEM) is provided, slope values along the evacuation route are used to adjust walking speed, allowing terrain-dependent evacuation time estimation.

- **Output generation**:
  After successful execution, 2 output layers will generate, first is buildings which are at risk and second is evacuation routes. Each building is assigned to the nearest evacuation shelter and that shelter’s ID and evacuation time is added in that building’s attribute. 
Buildings are classified according to evacuation time categories for further spatial analysis and visualization.

# Availability
The source code for Building-level Shortest Evacuation Time is openly available at:
https://github.com/gauravbkhairnar/Build_Short_Evac_Time_QGIS_Plugin

The plugin is distributed under the MIT License. It is designed to operate within the QGIS environment and can be installed through the QGIS Plugin Manager or manually from the repository. The project documentation, installation instructions, and example usage are provided in the repository README.

# Acknowledgements

This plugin utilizes road network data obtained from OpenStreetMap, a collaborative mapping initiative supported by contributors worldwide. The authors gratefully acknowledge the OpenStreetMap community for providing openly accessible geospatial data. The authors also extend their appreciation to the developers of QGIS Plugin Builder for their valuable tool and support. Furthermore, the authors express their sincere gratitude to the Director INCOIS and Ministry of Earth Sciences for providing the necessary infrastructure, research facilities, and financial support. The institutional guidance and support were instrumental in the successful completion of this research.


