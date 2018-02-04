# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# J_IMS_FieldCalc_inSettlement.py
# Created on: 2017-11-09 09:44:13.00000
#   (generated by ArcGIS/ModelBuilder)
# written for UNIFIL JGIS by Michael Iseli
# Description:
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy



# select all incidents within a village plus a 100m buffer
# set field value for inBuiltUpA to YES
# switch selection
# set field value for inBuiltUpA to NO
# clear selection



# Local variables:
SOIR_Analysis = "H:\\12e_Analysis\\Analysis.gdb\\SOIR_View\\SOIR_Analysis"
SOIR_Analysis_Layer = "SOIR_Analysis_Layer"
SOIR_Analysis_Layer__2_ = SOIR_Analysis_Layer
BuiltUpA_RL_filled = "H:\\12e_Analysis\\Analysis.gdb\\BaseData\\BuiltUpA_RL_filled"
SettlementLayer = "BuiltUpA_RL_filled_Layer"
SOIR_Analysis__4_ = SOIR_Analysis_Layer__2_
SOIR_Analysis__5_ = SOIR_Analysis__4_
SOIR_Analysis__2_ = SOIR_Analysis__5_
SOIR_Analysis_Layer_2_ = SOIR_Analysis__2_

# Process: Make Feature Layer
arcpy.MakeFeatureLayer_management(SOIR_Analysis, SOIR_Analysis_Layer, "", "", "OBJECTID_1 OBJECTID_1 VISIBLE NONE;Shape Shape VISIBLE NONE;OBJECTID OBJECTID VISIBLE NONE;incID incID VISIBLE NONE;Sector Sector VISIBLE NONE;Severity Severity VISIBLE NONE;Category Category VISIBLE NONE;Type Type VISIBLE NONE;TypeCode TypeCode VISIBLE NONE;ReportedBy ReportedBy VISIBLE NONE;Source Source VISIBLE NONE;Date Date VISIBLE NONE;Time Time VISIBLE NONE;Location Location VISIBLE NONE;UTM UTM VISIBLE NONE;QQQ QQQ VISIBLE NONE;Confirmati Confirmati VISIBLE NONE;FIR FIR VISIBLE NONE;StatusFIR StatusFIR VISIBLE NONE;SOI SOI VISIBLE NONE;StatusSOI StatusSOI VISIBLE NONE;DAIR DAIR VISIBLE NONE;StatusDAIR StatusDAIR VISIBLE NONE;EmailFromJ EmailFromJ VISIBLE NONE;FlagFromJO FlagFromJO VISIBLE NONE;EmailToJOC EmailToJOC VISIBLE NONE;FlagToJOC FlagToJOC VISIBLE NONE;StatusFina StatusFina VISIBLE NONE;Updated Updated VISIBLE NONE;Remark Remark VISIBLE NONE;created_us created_us VISIBLE NONE;created_da created_da VISIBLE NONE;last_edite last_edite VISIBLE NONE;last_edi_1 last_edi_1 VISIBLE NONE;SDE_STATE_ SDE_STATE_ VISIBLE NONE;DayNUM DayNUM VISIBLE NONE;MonthInc MonthInc VISIBLE NONE;YearInc YearInc VISIBLE NONE;MonthNum MonthNum VISIBLE NONE;MonthAge MonthAge VISIBLE NONE;WeekNUM WeekNUM VISIBLE NONE;BATT BATT VISIBLE NONE;WEIincS WEIincS VISIBLE NONE;WEIincA WEIincA VISIBLE NONE;incWEIGHT incWEIGHT VISIBLE NONE;RdType RdType VISIBLE NONE;InPosn InPosn VISIBLE NONE;InBuiltUp_A InBuiltUp_A VISIBLE NONE;NoPeople_Inc NoPeople_Inc VISIBLE NONE;WeekDayNUM WeekDayNUM VISIBLE NONE;Municipality Municipality VISIBLE NONE;Night Night VISIBLE NONE;IVO_BL IVO_BL VISIBLE NONE;WeightAge WeightAge VISIBLE NONE;THR_Relevance THR_Relevance VISIBLE NONE;TotalTHR_Weight TotalTHR_Weight VISIBLE NONE;GRID_ID GRID_ID VISIBLE NONE;WeekNUMyear WeekNUMyear VISIBLE NONE;MUN_OID MUN_OID VISIBLE NONE;yearcount yearcount VISIBLE NONE")

# Process: Make Feature Layer (2)
arcpy.MakeFeatureLayer_management(BuiltUpA_RL_filled, SettlementLayer, "", "", "OBJECTID OBJECTID VISIBLE NONE;Shape Shape VISIBLE NONE;Name Name VISIBLE NONE;OGL_code OGL_code VISIBLE NONE;level_ level_ VISIBLE NONE;DomPol DomPol VISIBLE NONE;DomRel DomRel VISIBLE NONE;Village_Color Village_Color VISIBLE NONE;Shape_Length Shape_Length VISIBLE NONE;Shape_Area Shape_Area VISIBLE NONE")

# Process: SelectFeatures_inSettlement
arcpy.SelectLayerByLocation_management(SOIR_Analysis_Layer, "INTERSECT", SettlementLayer, "100 Meters", "NEW_SELECTION", "NOT_INVERT")

# Process: Calculate_Field_inBuiltUpA_YES
arcpy.CalculateField_management(SOIR_Analysis_Layer__2_, "InBuiltUp_A", "1", "VB", "")

# Process: SwitchSelection
arcpy.SelectLayerByLocation_management(SOIR_Analysis__4_, "INTERSECT", "", "", "SWITCH_SELECTION", "NOT_INVERT")

# Process: Calculate_Field_ProxBL_NO
arcpy.CalculateField_management(SOIR_Analysis__5_, "InBuiltUp_A", "0", "VB", "")

# Process: ClearSelection
arcpy.SelectLayerByAttribute_management(SOIR_Analysis__2_, "CLEAR_SELECTION", "")




# return message that the code completed
print ("CALCULATION FIELD InBuiltUp_A COMPLETED")
