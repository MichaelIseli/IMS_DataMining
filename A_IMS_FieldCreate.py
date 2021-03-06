# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# A_IMS_FieldCreate_AMD01.py
# Created on: 2017-11-06 13:35:33.00000
#   (generated by ArcGIS/ModelBuilder)
# written for UNIFIL JGIS by Michael Iseli
# Description:
# ---------------------------------------------------------------------------



# Creation of field required for monthly analysis work with IMS incidents


# Import arcpy module
import arcpy








# Local variables:
SOIR_Analysis = "H:\\12e_Analysis\\Analysis.gdb\\SOIR_View\\SOIR_Analysis"
SOIR = SOIR_Analysis
SOIR_asOf_17July2014__6_ = SOIR
SOIR_asOf_17July2014__3_ = SOIR_asOf_17July2014__6_
SOIR_asOf_17July2014__4_ = SOIR_asOf_17July2014__3_
SOIR_asOf_17July2014__2_ = SOIR_asOf_17July2014__4_
SOIR_150728__2_ = SOIR_asOf_17July2014__2_
SOIR_150728__3_ = SOIR_150728__2_
SOIR_150728__4_ = SOIR_150728__3_
SOIR_150731__5_ = SOIR_150728__4_
SOIR_150731__2_ = SOIR_150731__5_
SOIR_150731__3_ = SOIR_150731__2_
SOIR_150731__4_ = SOIR_150731__3_
SOIR_150731__6_ = SOIR_150731__4_
SOIR_150731__7_ = SOIR_150731__6_
SOIR_asOf_17July2014__5_ = SOIR_150731__7_
SOIR_150728__5_ = SOIR_asOf_17July2014__5_
SOIR_150728__6_ = SOIR_150728__5_
SOIR_150728__7_ = SOIR_150728__6_
SOIR_150728__8_ = SOIR_150728__7_
SOIR_150728__9_ = SOIR_150728__8_
SOIR_150728__10_ = SOIR_150728__9_
SOIR_150728__11_ = SOIR_150728__10_
SOIR_150728__12_ = SOIR_150728__11_
SOIR_150728__13_ = SOIR_150728__12_
SOIR_150728__14_ = SOIR_150728__13_

# Process: Add Field_DayNUM
arcpy.AddField_management(SOIR_Analysis, "DayNUM", "SHORT", "", "", "", "Day", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field_MonthInc
arcpy.AddField_management(SOIR, "MonthInc", "SHORT", "", "", "", "Month", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field_YearNUM
arcpy.AddField_management(SOIR_asOf_17July2014__6_, "YearInc", "SHORT", "", "", "", "Years", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field_MonthNum
arcpy.AddField_management(SOIR_asOf_17July2014__3_, "MonthNum", "SHORT", "", "", "", "MonthNumber", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field_MonthAge
arcpy.AddField_management(SOIR_asOf_17July2014__4_, "MonthAge", "SHORT", "", "", "", "MonthAge", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field_WeekNUM
arcpy.AddField_management(SOIR_asOf_17July2014__2_, "WeekNUM", "SHORT", "", "", "", "WeekNUM", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field_BATTname
arcpy.AddField_management(SOIR_150728__2_, "BATT", "TEXT", "", "", "30", "BATT", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field_WEIincS
arcpy.AddField_management(SOIR_150728__3_, "WEIincS", "FLOAT", "2", "2", "", "Weight_incSource", "NULLABLE", "NON_REQUIRED", "WEIincS")

# Process: Add Field_WEIincA
arcpy.AddField_management(SOIR_150728__4_, "WEIincA", "FLOAT", "2", "2", "", "Weight_incAssess", "NULLABLE", "NON_REQUIRED", "WEIincA")

# Process: Add Field_incWEIGHT
arcpy.AddField_management(SOIR_150731__5_, "incWEIGHT", "FLOAT", "2", "2", "", "incWEIGHT", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field_RdType
arcpy.AddField_management(SOIR_150731__2_, "RdType", "SHORT", "2", "2", "", "RoadType", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field_InPosn
arcpy.AddField_management(SOIR_150731__3_, "InPosn", "SHORT", "1", "2", "", "Inside_FIL_Posn", "NULLABLE", "NON_REQUIRED", "YES_NO")

# Process: Add Field_InBuiltUp_A
arcpy.AddField_management(SOIR_150731__4_, "InBuiltUp_A", "SHORT", "1", "2", "", "In_BuiltUp_Area", "NULLABLE", "NON_REQUIRED", "YES_NO")

# Process: Add Field_NoPeopleInc
arcpy.AddField_management(SOIR_150731__6_, "NoPeople_Inc", "SHORT", "2", "2", "", "No_People_Inc", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field_WeekDayNUM
arcpy.AddField_management(SOIR_150731__7_, "WeekDayNUM", "SHORT", "", "", "", "WeekdayNumber", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field_Municipality
arcpy.AddField_management(SOIR_asOf_17July2014__5_, "Municipality", "TEXT", "", "", "75", "Municipality", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field_Night_Y_N
arcpy.AddField_management(SOIR_150728__5_, "Night", "SHORT", "1", "", "30", "Night_Y_N", "NULLABLE", "NON_REQUIRED", "YES_NO")

# Process: Add Field_IVO_BL
arcpy.AddField_management(SOIR_150728__6_, "IVO_BL", "SHORT", "1", "", "30", "IVO_BL", "NULLABLE", "NON_REQUIRED", "YES_NO")

# Process: Add Field_WeigthAge
arcpy.AddField_management(SOIR_150728__7_, "WeightAge", "FLOAT", "1", "", "30", "WeightAge", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field_THR_Relevance
arcpy.AddField_management(SOIR_150728__8_, "THR_Relevance", "FLOAT", "1", "", "30", "THR_Relevance", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field_TotalTHR_Weight
arcpy.AddField_management(SOIR_150728__9_, "TotalTHR_Weight", "FLOAT", "1", "", "30", "TotalTHR_Weight", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field_GRID_ID
arcpy.AddField_management(SOIR_150728__10_, "GRID_ID", "TEXT", "1", "", "12", "GRID_ID", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field_WeekNUMyear
arcpy.AddField_management(SOIR_150728__11_, "WeekNUMyear", "SHORT", "1", "", "12", "WeekNUMyear", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field_MUN_OID
arcpy.AddField_management(SOIR_150728__12_, "MUN_OID", "SHORT", "1", "", "12", "WeekNUMyear", "NULLABLE", "NON_REQUIRED", "")

# Process: Add Field_yearcount
arcpy.AddField_management(SOIR_150728__13_, "yearcount", "SHORT", "1", "", "12", "yearcount", "NULLABLE", "NON_REQUIRED", "")




# return message that the code completed
print ("FIELD CREATION COMPLETED")

