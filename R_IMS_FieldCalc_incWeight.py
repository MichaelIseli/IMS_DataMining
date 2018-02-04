# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# R_IMS_FieldCalc_incWeight.py
# Created on: 2018-02-01 21:21:59.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
SOIR_Analysis = "SOIR_Analysis"
SOIR_Analysis__3_ = SOIR_Analysis

# Process: Calculate Field
arcpy.CalculateField_management(SOIR_Analysis, "incWEIGHT", "[WEIincS]* [WEIincA]", "VB", "")

