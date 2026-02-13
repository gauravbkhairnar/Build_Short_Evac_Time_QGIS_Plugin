<table>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/2810615e-b2d5-4201-8b8a-fda02d84e71a" width="620"/>
    </td>
    <td>
      <h1>Build_Short_Evac_Time_QGIS_Plugin</h1>
      <p>A QGIS plugin for computing building-level evacuation planning. It automatically identifies buildings located within a flood inundation area and computes the shortest evacuation routes from these at-risk buildings to designated safe shelters.</p>
    </td>
  </tr>
</table>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
## General Information
<p>
  This plugin automatically identifies buildings located within a tsunami or flood inundation area and computes the shortest evacuation routes from these at-risk buildings to designated safe shelters. The analysis is performed using minimal user inputs and leverages OpenStreetMap (OSM) road networks to generate evacuation paths.
</p>
<p>
  The tool is designed to support rapid evacuation planning and scenario-based analysis by providing building-level evacuation routes that can be visualised directly within QGIS or exported for further use. This plugin is particularly useful for coastal hazard preparedness, evacuation planning, and disaster risk assessment studies.
</p>

## Installation
> **__Note:__**
> This plugin requires additional Python packages. Please download and install the packages in [requirement.txt](https://github.com/gauravbkhairnar/Build_Short_Evac_Time_QGIS_Plugin/blob/main/requirements.txt) 
 
### Installation of Prerequisites:
  
  #### For Windows:
  * Copy filepath --> Start --> Open OSGeo4W Shell --> cd (paste filepath) --> Enter -->
  * paste this 
  ```bash
	pip install -r requirements.txt
```

  #### For Linux:
  * Open terminal --> cd filepath -->
  * paste this
    
    ```bash
	python3 -m pip install --user -r requirements.txt
	```
    
  ### Restart QGIS
  
### Online installation (QGIS) :
  * Open QGIS -> Plugins -> Manage and Install Plugins... -> "All" tab (in right pannel) -> search for 'Build_Short_Evac_Time' --> select and install plugin
 
### Offline installation :
  * Go to the [releases](https://github.com/gauravbkhairnar/Build_Short_Evac_Time_QGIS_Plugin/releases/tag/QGIS_Plugin) section of this repository, --> download the .zip file.
  * Rename the downloaded zip file to build_short_evac_time.zip
  * Open QGIS --> Plugins --> Manage and Install Plugins... --> install from ZIP tab --> select the renamed zip --> install plugin (If any warnings appear during installation, they can be safely ignored).

## Input required:

  All the input data are in vector format with extensions .shp or .geojson
All input datasets must be vector layers in one of the supported formats:

* Shapefile(.shp)
* Geojosn (.geojson)

The following layers are required:
1. Building Layer (Geometry type: Polygon)
2. Evacuation Shelters Layer (Geometry type: Point)
3. Flood Inundation Layer (Geometry type: Polygon)

> **__Note:__**
> * All input layers must be projected in EPSG:4326 (WGS 84) to ensure correct spatial analysis and routing.
> * Please create an 'id' field in the Evacuation Shelter layer and assigned unique id to each Evacuation Shelter. 

## Step-by-Step workflow
## Step 1: Open the Plugin
After successful installation, QGIS --> Plugins --> build_short_evac_time --> Build Shortest Evacuation Time. As shown in the figure below.
<img width="976" height="217" alt="start" src="https://github.com/user-attachments/assets/c843d463-bd79-49d8-8e48-1f57694d44c6" />

## Step 2: Select Input Layers
* If the Buildings, Evacuation Shelters, and Flood Inundation layers are already loaded in the QGIS Layers Panel, select them using the respective dropdown menus.
* Alternatively, use the Browse buttons to select input layers directly from disk without adding them to the Layers Panel
## Step 3: Select Output Folder (Optional)
* Specify an output folder where the results will be saved.
* If no output folder is provided, the plugin will automatically create temporary layers in memory.
## Step 4: Run the Model
Steps are shown in the Figure below:
<img width="940" height="601" alt="image" src="https://github.com/user-attachments/assets/70613a28-ddcb-44f7-8259-a9a09a6bbf51" />

## Output
After successful execution, the output layers will be added to the QGIS Layers Panel:
1.	buildings_with_clusters
* Contains buildings identified as requiring evacuation.
* Includes building-level evacuation attributes.
2.	Evacuation_Routes
* Represents the shortest walking routes from the nearest node from building to its assigned evacuation shelter.

## Output Attributes
* Each building is assigned to the nearest evacuation shelter and that shelter’s ID and the shortest route is computed between each building and its assigned shelter.
* Walking time is calculated and stored in the Time field from the building to the shelter.

## Assumptions
* The evacuation mode during the inundation hazards is preferably by walking to avoid traffic congestion. Walking speed is considered as 4.68 m/s
* All evacuees are assumed to be physically fit adults capable of walking without assistance.
* The road network derived from OpenStreetMap is assumed to be fully passable and in good condition for evacuation. The off-road evacuation was not considered.
* All evacuees are assumed to start from the nearest accessible node/junction on the road network. The distance from each building to the nearest junction and the walking time within the building (in case of a big building/multi-story) are not considered.  
* Terrain is assumed to be flat; slopes along the routes are not considered.

## Exceptions and Special Conditions
* No Buildings in the Flood Zone
If no buildings intersect with the flood inundation zone, the process terminates automatically and a message is displayed:
“No Buildings in the Flood Zone”
* All Shelters Within Flood Zone
If all evacuation shelters fall within the flooding/inundation area, the process terminates and the following message is shown:
“All evacuation shelters are in the flood zone”
* Road Network Not Available
If no OpenStreetMap (OSM) pedestrian road network is found in the vicinity of the buildings, the process stops and a warning message is displayed:
“Road Network Not Found”


> **__Note:__**
> * The model executes using sequential processing; parallel or multiprocessing is not currently implemented.
> * Sample datasets for the Build Shortest Evacuation Time plugin are provided in the [sample data](https://github.com/gauravbkhairnar/Build_Short_Evac_Time_QGIS_Plugin/tree/main/sample_data) folder for testing and demonstration purposes.

## Development Team:
Gaurav Khairnar, RS Mahendra, Ch Patanjali, TNC Kartik, Sudheer Joseph, TM Balakrishnan Nair 

Affiliation: Indian National Centre for Ocean Information Services (INCOIS), Ministry of Earth Sciences, Hyderabad

## References:
Putra, H., Kemal, B. M., & Mas, E. (2020, February). Identification of factors influencing the evacuation walking speed in Padang, Indonesia. In 2nd International Symposium on Transportation Studies in Developing Countries (ISTSDC 2019) (pp. 125-130). Atlantis Press.

Srinivasa Kumar, T., & Manneela, S. (2021). A review of the progress, challenges and future trends in tsunami early warning systems. Journal of the Geological Society of India, 97(12), 1533-1544

Universal Transverse Mercator coordinate system – Wikipedia
https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system















