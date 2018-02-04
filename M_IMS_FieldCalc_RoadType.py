# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# M_IMS_FieldCalc_RoadType.py
# Created on: 2018-02-01 21:04:53.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
SOIR_Analysis = "SOIR_Analysis"
Inc_25m_from_TertiaryRd = SOIR_Analysis
RoadL_AO = "RoadL_AO"
RoadL_selection = RoadL_AO
Inc_TertiaryRd = Inc_25m_from_TertiaryRd
Inc_25m_from_SecondaryRd = Inc_TertiaryRd
RoadL_AO__2_ = "RoadL_AO"
RoadL_selection__2_ = RoadL_AO__2_
Inc_SecondaryRd = Inc_25m_from_SecondaryRd
Inc_25m_from_PrimaryRd__2_ = Inc_SecondaryRd
RoadL_AO__3_ = "RoadL_AO"
RoadL_selection__3_ = RoadL_AO__3_
Inc_SecondaryRd__2_ = Inc_25m_from_PrimaryRd__2_
Inc_25m_from_PrimaryRd__3_ = Inc_SecondaryRd__2_
RoadL_AO__4_ = "RoadL_AO"
RoadL_selection__4_ = RoadL_AO__4_
Inc_SecondaryRd__3_ = Inc_25m_from_PrimaryRd__3_

# Process: Select Tertiary & Unkn Roads
arcpy.SelectLayerByAttribute_management(RoadL_AO, "NEW_SELECTION", "rtt = 16 OR rtt = 17 OR rtt = 18 OR rtt = 0")

# Process: Select Layer By Location
arcpy.SelectLayerByLocation_management(SOIR_Analysis, "INTERSECT", RoadL_selection, "25 Meters", "NEW_SELECTION", "NOT_INVERT")

# Process: Calculate Field
arcpy.CalculateField_management(Inc_25m_from_TertiaryRd, "RdType", "4", "VB", "")

# Process: Select SecondaryRd
arcpy.SelectLayerByAttribute_management(RoadL_AO__2_, "NEW_SELECTION", "rtt = 14")

# Process: Select Layer By Location (2)
arcpy.SelectLayerByLocation_management(Inc_TertiaryRd, "INTERSECT", RoadL_selection__2_, "25 Meters", "NEW_SELECTION", "NOT_INVERT")

# Process: Calculate Field (2)
arcpy.CalculateField_management(Inc_25m_from_SecondaryRd, "RdType", "3", "VB", "")

# Process: Select PrimaryRd
arcpy.SelectLayerByAttribute_management(RoadL_AO__3_, "NEW_SELECTION", "rtt = 13")

# Process: Select Layer By Location (3)
arcpy.SelectLayerByLocation_management(Inc_SecondaryRd, "INTERSECT", RoadL_selection__3_, "25 Meters", "NEW_SELECTION", "NOT_INVERT")

# Process: Calculate Field (3)
arcpy.CalculateField_management(Inc_25m_from_PrimaryRd__2_, "RdType", "2", "VB", "")

# Process: Select HighWay
arcpy.SelectLayerByAttribute_management(RoadL_AO__4_, "NEW_SELECTION", "rtt = 15")

# Process: Select Layer By Location (4)
arcpy.SelectLayerByLocation_management(Inc_SecondaryRd__2_, "INTERSECT", RoadL_selection__4_, "25 Meters", "NEW_SELECTION", "NOT_INVERT")

# Process: Calculate Field (4)
arcpy.CalculateField_management(Inc_25m_from_PrimaryRd__3_, "RdType", "1", "VB", "")

