# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 17:46:51 2019

@author: My PC
"""

import arcpy, os
from arcpy import env
import osmnx as ox
import numpy as np
import networkx as nx
import geopandas as gpd
import pandas as pd
from shapely.geometry import shape
import fiona
print ("modules imported")

arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")
#specify data input location
input_data = "D:\phd\Sandy"
arcpy.env.workspace = input_data

urban_deposits = "new_urban.shp"
buffered_urban = "urban_b.shp"
#create buffer around deposits
arcpy.Buffer_analysis(urban_deposits, buffered_urban, "100 METERS")

new_fields = ("new_area","s_length","sdensity", "n_density", "s_per_node", "i_density", "i_count")
#add fields in attribute table for urban variables from osmnx
for i in new_fields:
    arcpy.AddField_management(buffered_urban, i, "LONG")
    expression1 = "{0}".format("!SHAPE.area@SQUAREMETERS!")
    #calculate buffer area
    arcpy.CalculateField_management(buffered_urban, "new_area", expression1, "PYTHON", )

#loop through polygons within the shapefile to do osmnx 

with arcpy.da.UpdateCursor(buffered_urban, ["Shape@", "new_area", "s_length", "s_density", "i_density"]) as cursor:
    for row in cursor:
        area = row[1]
        geom = shape(row[0])
        G6 = ox.graph_from_polygon(geom, network_type='drive_service')
        G6_projected = ox.project_graph(G6)
        fig, ax = ox.plot_graph(G6_projected)
        stats = ox.stats.basic_stats(G6_projected, area)
        row[2] = stats['street_length_total']
        row[3] = stats['street_density_km']
        row[4] = stats['intersection_density_km']
        cursor.updateRow(row)
        
print ("finished")