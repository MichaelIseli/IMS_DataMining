#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      iseli
#
# Created:     07/11/2017
# Copyright:   (c) iseli 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# calculation of incident confirmation value in the formula for overall incident weight
# if inc is "observed by UNIFIL" value is 1
# elif inc is "Confirmed by UNIFIL" value is 1
# elif inc is "Partially confirmed by UNIFIL" value is 0.70
# elif inc is "Not confirmed by UNIFIL" value is 0.50
# elif inc is "Refuted by UNIFIL" value is 0.00



# Import arcpy module
import arcpy

# Local variables
SOIR_Analysis = "J:\\12e_Analysis\\Analysis.gdb\\SOIR_View\\SOIR_Analysis"


var1 = "Confirmati"

if var1 = "Confirmed by UNIFIL"
    print "1"

elif var1 = "Observed by UNIFIL"
    print "1"

elif var1 = "Partially confirmed by UNIFIL"
    print "0.70"