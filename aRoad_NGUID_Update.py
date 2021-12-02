import arcpy
from arcpy import env
import os
import datetime
import pandas as pd
from arcgis import GIS

wrkspc = env.wrkspc = r'E:\GIS\DailyData\MXDs\ArcGIS_Pro_Projects\8-25-20-Tommy\8-25-20-Tommy.gdb'
road_FC = 'Standard Working Data\\Online_MC_Layers\\RoadCenterlines'
parcels = 'Parcels'


def findMaxRoadNGUID(wrkspc, road_FC):
    arcpy.management.SelectLayerByAttribute(road_FC, 'CLEAR_SELECTION') 
    fldlist=['RCL_NGUID'] #This is pulling in the geometry
    cursor = arcpy.da.SearchCursor(road_FC,fldlist) # Defining the SearchCursor 
    fld_name_list=cursor.fields #Defining the fields within the "road_FC" dataset
    search_field="RCL_NGUID" #Defining the field that I am interested in
    indx=fld_name_list.index(search_field) # Obtaining the index number from the tuple of field names. This is instead of using fld_name_list[6]
    nguid=[]
    global RCL_NGUID 
    RCL_NGUID = 0
    p=0
    if search_field in fld_name_list:
        print('Yes, ' + search_field + ' is in the table')
        for row in cursor:
            print(row[indx])
            tempNGUID = row[indx]
            if tempNGUID is None:
                print('Value is None')
                p +=1
            elif tempNGUID == '':
                print('Value is None')
                p +=1
            else:
                nguidNumber=int(row[indx][12:])
                print(str(nguidNumber) + "  is an interger")
                if RCL_NGUID < nguidNumber:
                    RCL_NGUID = nguidNumber
                    print(nguidNumber)
                print(RCL_NGUID)
    else:
        print('The field that you are looking for is not in the data.')
    print('Script Complete\n\n\tThe number of records without an RCL_NGUID is: \t' + str(p))
    #SelectSendLetterRecordsWithoutNGUID()
    return RCL_NGUID
    #print('RCL_NGUID is:  ' + str(RCL_NGUID))

RCL_NGUID = findMaxRoadNGUID(wrkspc, road_FC)
print('\n\n\tMax RCL_NGUID is:   ' + str(RCL_NGUID) + "\n")



def SelectUpdateRecordsWithoutNGUID():
    arcpy.management.SelectLayerByAttribute(road_FC, 'CLEAR_SELECTION')
    arcpy.management.SelectLayerByAttribute(road_FC, "NEW_SELECTION", '''RCL_NGUID IS NULL''', None) # This stopped working after an update.
    arcpy.management.SelectLayerByAttribute(road_FC, 'ADD_TO_SELECTION',"RCL_NGUID = ''",None)
    count = arcpy.management.GetCount(road_FC)
    print('The number of records without an NGUID is:  ' + str(count) + '\n\n')
    # To add in the future: https://support.esri.com/en/technical-article/000023601

SelectUpdateRecordsWithoutNGUID()


recImport = "autoIncrement(" + str(RCL_NGUID) + ")"
arcpy.management.CalculateField(road_FC, "RCL_NGUID", recImport, "PYTHON3", '''rec = RCL_NGUID
def autoIncrement(RCL_NGUID):
    global rec
    print(rec)
    pStart = 99999
    pInterval = 1
    if (rec == 0):
        rec = pStart
    else:
        rec = rec + pInterval
    return "STR.MADISON." + str(rec).zfill(5)''', "TEXT")


def ClearSelectedRecords():
    arcpy.management.SelectLayerByAttribute(road_FC, 'CLEAR_SELECTION') 
ClearSelectedRecords()






