# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# C_IMS_FieldCalc_MonthNum.py
# Created on: 2017-11-06 14:53:54.00000
#   (generated by ArcGIS/ModelBuilder)
# written for UNIFIL JGIS by Michael Iseli
# Description:
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# code to calculate the field month number for IMS incident analysis


# Local variables:
SOIR_Analysis = "H:\\12e_Analysis\\Analysis.gdb\\SOIR_View\\SOIR_Analysis"
SOIR_Analysis__3_ = SOIR_Analysis

# Process: Calculate Field
arcpy.CalculateField_management(SOIR_Analysis, "MonthNum", "(([yearcount]-1)*12)+ [MonthInc]", "VB", "")

# return message that the code completed
print ("CALCULATION FIELD MONTH NUMBER COMPLETED")