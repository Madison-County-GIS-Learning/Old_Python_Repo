#ArcGIS Pro Letter Automation 2021
import arcpy
from arcpy import env
import os
import datetime
import pandas as pd
from arcgis import GIS

wrkspc = env.wrkspc = r'E:\GIS\DailyData\MXDs\ArcGIS_Pro_Projects\8-25-20-Tommy\8-25-20-Tommy.gdb'
#wrkspc = env.wrkspc = r'C:\Users\TLuksha\Desktop\MailingAppendLetters\CreateNewStructures\CreateNewStructures.gdb'
#wrkspc=r"E:\GIS\DailyData\MXDs\ArcGIS_Pro_Projects\8-25-20-Tommy\8-25-20-Tommy.gdb"
#arcpy.env.wrkspc = wrkspc
#wrkspc=r"E:\GIS\DailyData\MXDs\ArcGIS_Pro_Projects\8-25-20-Tommy\8-25-20-Tommy.gdb"
#structures = r"Standard Working Data\Online_MC_Layers\SiteStructureAddressPoints"
MailingLettersFolder = r"C:\Users\TLuksha\Desktop\MailingAppendLetters"
#fc = r"Standard Working Data\Online_MC_Layers\SiteStructureAddressPoints"
#fc = 'Online_MC_Layers\\SiteStructureAddressPoints'
fc = "Standard Working Data\\Online_MC_Layers\\SiteStructureAddressPoints"
#fc = "https://services7.arcgis.com/xh3dsZbIkSAmWWRV/arcgis/rest/services/NG911_CoreData/FeatureServer/1"
#test_fc = r'C:\Users\TLuksha\Desktop\MailingAppendLetters\CreateNewStructures.gdb\FailedStructureMod07272021'
#fc = test_fc
## Try this following line when running through the IDE
#gis = GIS(profile="Tommy_AGOL_prof")
#parcels = 'Parcels'
parcels = r"Standard Working Data\Parcels"
#parcels = r"https://gistestservicemt.gov/arcgis/rest/services/MSDI_Framework/Parcels/MapServer/0"
YellowstoneClub = "Standard Working Data\\Neighborhoods\\YellowstoneClub"
Moonlight_Basin = "Standard Working Data\\Neighborhoods\\Moonlight_Basin"
Spanish_Peaks = "Standard Working Data\\Neighborhoods\\Spanish_Peaks"
WordMergeDoc = r"C:\Users\TLuksha\Desktop\Mail Merge Letter 2.docx"

def SelectSendLetterRecords():
    sendLetterqry = '"SendLetter" = 1' 
    arcpy.management.SelectLayerByAttribute(fc, 'NEW_SELECTION', sendLetterqry)
    count = arcpy.management.GetCount(fc)
    print('The number of  SendLetter  records selected is:  ' + str(count) + '\n')    
    # To add in the future: https://support.esri.com/en/technical-article/000023601
SelectSendLetterRecords()


## Unit = Unit.strip(()



arcpy.management.CalculateField(fc, "Post_Comm", "ReclassPostalCode(!Post_Code!)", "PYTHON3", '''def ReclassPostalCode(Post_Comm):
    if (str(Post_Comm) == "59701"):
        return "Butte"
    elif (str(Post_Comm) == "59710"):
        return "Alder"
    elif (str(Post_Comm) == "59716"):
        return "Big Sky"
    elif (str(Post_Comm) == "59718"):
        return "Bozeman"
    elif (str(Post_Comm) == "59720"):
        return "Cameron"
    elif (str(Post_Comm) == "59721"):
        return "Cardwell"
    elif (str(Post_Comm) == "59725"):
        return "Dillon"
    elif (str(Post_Comm) == "59729"):
        return "Ennis"
    elif (str(Post_Comm) == "59730"):
        return "Gallatin Gateway"
    elif (str(Post_Comm) == "59732"):
        return "Melrose"
    elif (str(Post_Comm) == "59735"):
        return "Harrison"
    elif (str(Post_Comm) == "59739"):
        return "Dillon"
    elif (str(Post_Comm) == "59740"):
        return "McAllister"
    elif (str(Post_Comm) == "59743"):
        return "Melrose"
    elif (str(Post_Comm) == "59745"):
        return "Norris"
    elif (str(Post_Comm) == "59747"):
        return "Pony"
    elif (str(Post_Comm) == "59749"):
        return "Sheridan"
    elif (str(Post_Comm) == "59751"):
        return "Silver Star"
    elif (str(Post_Comm) == "59752"):
        return "Three Forks"
    elif (str(Post_Comm) == "59754"):
        return "Twin Bridges"
    elif (str(Post_Comm) == "59755"):
        return "Virginia City"
    elif (str(Post_Comm) == "59758"):
        return "West Yellowstone"
    elif (str(Post_Comm) == "59759"):
        return "Whitehall"
    elif (str(Post_Comm) == "59760"):
        return "Willow Creek"
    else:
        return "--UNKNOWN--"''', "TEXT")


def ReclassAttributes(wrkspc,fc):
    #1	Source	Planning
    # Add an If THEN statement. If = "Structures" then update.
    #arcpy.management.CalculateField(fc, "Source", "'PLANNING'", "PYTHON3", '', "TEXT")
    
    arcpy.management.CalculateField(fc, "County", '"MADISON"', "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")
    arcpy.management.CalculateField(fc, "State", '"MT"', "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")
    arcpy.management.CalculateField(fc, "Country", '"US"', "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")
    
    #32	Post_Comm	
    arcpy.management.CalculateField(fc, "Post_Comm", "ReclassPostalCode(!Post_Code!)", "PYTHON3")
    
    #43	Place_Type	'unknown'
    arcpy.management.CalculateField(fc, "Place_Type", "'unknown'", "PYTHON3", '', "TEXT")
    
    #44	Placement	Unknown'
    arcpy.management.CalculateField(fc, "Placement", "'Unknown'", "PYTHON3", '', "TEXT")
    
    #53	FullRoadName	
    arcpy.management.CalculateField(fc, "FullRoadName", '" ".join([str(i) for i in [ !LSt_PreType!, !LSt_PreDir!, !LSt_Name!, !LSt_Type!,!LSt_PosDir!] if i])', "PYTHON3", '', "TEXT") # Replaced on 10/29/21 due to unintentional spaces from the new planning department temp dataset.
    arcpy.management.CalculateField(fc, "FullRoadName", '!FullRoadName!.strip()', "PYTHON3", '', "TEXT")
    #arcpy.management.CalculateField(fc, "FullRoadName", '" ".join([str(i) for i in [ !LSt_PreType!.replace(" ", ""), !LSt_PreDir!.replace(" ", ""), !LSt_Name!.replace(" ", ""), !LSt_Type!.replace(" ", ""),!LSt_PosDir!.replace(" ", "")] if i])', "PYTHON3", '', "TEXT") 
    #arcpy.management.CalculateField(fc, "FullRoadName", '" ".join([str(i) for i in [!LSt_PreDir!.replace(" ", ""), !LSt_PreType!.replace(" ", ""), !LSt_Name!, !LSt_Type!.replace(" ", ""), !LSt_PosDir!.replace(" ", "")] if i])', "PYTHON3", '', "TEXT")
    
    #54	FullAddress	
    arcpy.management.CalculateField(fc, "FullAddress", "completeLabelField(!Add_Number!, !AddNum_Suf!, !LSt_PreType!, !LSt_PreDir!, !LSt_Name!, !LSt_Type!, !LSt_PosDir!, !Unit!) ", "PYTHON3", r'''def completeLabelField(Add_Number, AddNum_Suf, LSt_PreType, LSt_PreDir, LSt_Name, LSt_Type, LSt_PosDir, Unit): 
        if Unit is None:
            return " ".join([str(i) for i in [ Add_Number, AddNum_Suf, LSt_PreType, LSt_PreDir, LSt_Name, LSt_Type, LSt_PosDir] if i])
        else:
            return " ".join([str(i) for i in [ Add_Number, AddNum_Suf, LSt_PreType, LSt_PreDir, LSt_Name, LSt_Type, LSt_PosDir, "UNIT", Unit] if i])''', "TEXT")
    for n in range(3):
        arcpy.management.CalculateField(fc, "FullAddress", '''!FullAddress!.strip().replace('  ',' ')''', "PYTHON3", '', "TEXT")
    #arcpy.management.CalculateField(fc, "FullAddress", '''!FullAddress!.strip().replace('  ',' ')''', "PYTHON3", '', "TEXT") # for range is not validated yet.
    
    #55	FullRoadName_MSAGComm	
    arcpy.management.CalculateField(fc, "FullRoadName_MSAGComm", "!FullRoadName! + '_' + !MSAGComm!", "PYTHON3", '', "TEXT")
    
    #56	FullRoadName_ESN	
    arcpy.management.CalculateField(fc, "FullRoadName_ESN", '"".join([str(i) for i in [!FullRoadName!,"_",!ESN!] if i])', "PYTHON3", '', "TEXT")
    
    #57	FullAddress_MSAGComm	
    arcpy.management.CalculateField(fc, "FullAddress_MSAGComm", '"".join([str(i) for i in [!FullAddress!,"_",!MSAGComm!] if i])', "PYTHON3", '', "TEXT")
    
    #58	FullAddress_ESN	
    arcpy.management.CalculateField(fc, "FullAddress_ESN", '"".join([str(i) for i in [!FullAddress!,"_",!ESN!] if i])', "PYTHON3", '', "TEXT")
    
    #70	YEAR_BUILT	
    arcpy.management.CalculateField(fc, "YEAR_BUILT", "'9999'", "PYTHON3", '', "TEXT")
    
    ## Consider an If Then statement to pass if NULL for Geotext
    
    #71	GeoText	ParcelID
    #arcpy.management.CalculateField(fc, "GeoText", "!ParcelID!", "PYTHON3", '', "TEXT")
    #arcpy.management.CalculateField(fc, "GeoText", "!ParcelID!", "PYTHON3", '', "TEXT")
    
    #74	Siding	'Unknown'
    arcpy.management.CalculateField(fc, "Siding", "'Unknown'", "PYTHON3", '', "TEXT")
    
    #75	Roof	
    arcpy.management.CalculateField(fc, "Roof", "'Unknown'", "PYTHON3", '', "TEXT")
    
    #82	StrucType1	'NOT MAPPED OR VALIDATED PER PLANNING'
    arcpy.management.CalculateField(fc, "StrucType1", "'NOT MAPPED OR VALIDATED PER PLANNING'", "PYTHON3", '', "TEXT")
    
    #83	StrucType2	'NOT MAPPED OR VALIDATED PER PLANNING'
    arcpy.management.CalculateField(fc, "StrucType2", "'NOT MAPPED OR VALIDATED PER PLANNING'", "PYTHON3", '', "TEXT")
    
    #84	StrucType3	'NOT MAPPED OR VALIDATED PER PLANNING'
    arcpy.management.CalculateField(fc, "StrucType3", "'NOT MAPPED OR VALIDATED PER PLANNING'", "PYTHON3", '', "TEXT")
    
    # This label field update does not work: 
    #    arcpy.management.CalculateField(fc, "Label", "completeLabelField(!Add_Number!, !AddNum_Suf!, !LSt_PreType!, !LSt_PreDir!, !LSt_Name!, !LSt_Type!, !LSt_PosDir!, !Unit!) ", "PYTHON3", r"""def completeLabelField(Add_Number, AddNum_Suf, LSt_PreType, LSt_PreDir, LSt_Name, LSt_Type, LSt_PosDir, Unit):     if Unit is None:        return " ".join([str(i) for i in [ Add_Number, AddNum_Suf, LSt_PreType, LSt_PreDir, LSt_Name, LSt_Type, LSt_PosDir] if i])    else:        return " ".join([str(i) for i in [ Add_Number, AddNum_Suf, LSt_PreType, LSt_PreDir, LSt_Name, LSt_Type, LSt_PosDir, "UNIT", Unit] if i])""", "TEXT")
    
    #102	Label	
    #arcpy.management.CalculateField(fc, "Label", "completeLabelField(!Add_Number!, !AddNum_Suf!, !LSt_PreType!, !LSt_PreDir!, !LSt_Name!, !LSt_Type!, !LSt_PosDir!, !Unit!) ", "PYTHON3", r'''def completeLabelField(Add_Number, AddNum_Suf, LSt_PreType, LSt_PreDir, LSt_Name, LSt_Type, LSt_PosDir, Unit): 
        #if Unit is None:
            #return " ".join([str(i) for i in [ Add_Number, AddNum_Suf, LSt_PreType, LSt_PreDir, LSt_Name, LSt_Type, LSt_PosDir] if i])
        #else:
            #return " ".join([str(i) for i in [ Add_Number, AddNum_Suf, LSt_PreType, LSt_PreDir, LSt_Name, LSt_Type, LSt_PosDir, "UNIT", Unit] if i])''', "TEXT")

    arcpy.management.CalculateField(fc, "Label", "completeLabelField(!Add_Number!, !AddNum_Suf!, !LSt_PreType!, !LSt_PreDir!, !LSt_Name!, !LSt_Type!, !LSt_PosDir!, !Unit!) ", "PYTHON3", r'''def completeLabelField(Add_Number, AddNum_Suf, LSt_PreType, LSt_PreDir, LSt_Name, LSt_Type, LSt_PosDir, Unit): 
        if Unit is None:
            return " ".join([str(i) for i in [ Add_Number, AddNum_Suf, LSt_PreType, LSt_PreDir, LSt_Name, LSt_Type, LSt_PosDir] if i])
        else:
            return " ".join([str(i) for i in [ Add_Number, AddNum_Suf, LSt_PreType, LSt_PreDir, LSt_Name, LSt_Type, LSt_PosDir, "UNIT", Unit] if i])''', "TEXT")
    for n in range(3):
        arcpy.management.CalculateField(fc, "Label", '''!Label!.strip().replace('  ',' ')''', "PYTHON3", '', "TEXT")
ReclassAttributes(wrkspc,fc)

## Part 2 of script.... Join, populate, disjoin

def JoinParcelCompleteDataFields(fc):
    try:
        arcpy.management.RemoveJoin(fc, "L0Parcels")
    except:
        print('No Join Present')
    # Join Parcels to Structures in order to update fields
    arcpy.management.AddJoin(fc, 'ParcelID', parcels, 'PARCELID', 'KEEP_ALL')
    #arcpy.management.AddJoin(fc, 'ParcelID', 'Parcels', 'ParcelID', 'KEEP_ALL')
    # 72	SubdivName	
    arcpy.management.CalculateField(fc, "L1SiteStructureAddressPoints.SubdivName", "!L0Parcels.Subdivision!", "PYTHON3", '', "TEXT")
    #87	AssesText	
    arcpy.management.CalculateField(fc, "L1SiteStructureAddressPoints.AssesText", "!L0Parcels.AssessmentCode!", "PYTHON3", '', "TEXT")
    #88	LegalDescr	!LegalDescriptionShort!
    arcpy.management.CalculateField(fc, "L1SiteStructureAddressPoints.LegalDescr", "!L0Parcels.LegalDescriptionShort!", "PYTHON3", '', "TEXT")
    # Remove Parcel join with Structures
    arcpy.management.RemoveJoin(fc, "L0Parcels")
    # To add in the future: https://support.esri.com/en/technical-article/000023601

JoinParcelCompleteDataFields(fc)

def UpdateNeighborhoods(fc):
    ## Update attributes for YC, SP, Moonlight. 
    ## NEED TO MAKE INCORPORATED COMMUNITIES UPDATE OPTION
    
    # Update Yellowstone Club
    arcpy.management.SelectLayerByLocation(fc, "WITHIN", YellowstoneClub, None, "NEW_SELECTION", "NOT_INVERT")
    arcpy.management.CalculateField(fc, "Nbrhd_Comm", "'Yellowstone Club'", "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")
    arcpy.management.CalculateField(fc, "LetterTo", "'janet.earl@yellowstoneclub.com, sarah.blechta@yellowstoneclub.com, taylour.wilson@yellowstoneclub.com'", "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")

    # Update Moonlight Basin
    arcpy.management.SelectLayerByLocation(fc, "WITHIN", Moonlight_Basin, None, "NEW_SELECTION", "NOT_INVERT")
    arcpy.management.CalculateField(fc, "Nbrhd_Comm", "'Moonlight'", "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")
    
    #Update Spanish Peaks structures
    arcpy.management.SelectLayerByLocation(fc, "WITHIN", Spanish_Peaks, None, "NEW_SELECTION", "NOT_INVERT")
    arcpy.management.CalculateField(fc, "Nbrhd_Comm", "'Spanish Peaks'", "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")
#for n in range(5):
    #print("Need to fix the GDB located at: E:\GIS\DailyData\2020-File-Cleanup\Neighborhoods_Communities_Regions\Neighborhood_Communities.gdb"
          
#UpdateNeighborhoods(fc)

def UpdateIncorporatedAreas(fc):
    ## Will need to update this section to update incorporated areas.
    for i in range(5):
        print('Need to split and populate incorporated areas. Could also create layers in memory.\n')
UpdateIncorporatedAreas(fc)

def findMaxNGUID(wrkspc, fc):
    try:
        arcpy.management.RemoveJoin(fc, "L0Parcels")
        print('Join removed')
    except Exception:
        print('No Join was present')
    arcpy.management.SelectLayerByAttribute(fc, 'CLEAR_SELECTION') 
    fldlist=['Site_NGUID'] #This is pulling in the geometry
    cursor = arcpy.da.SearchCursor(fc,fldlist) # Defining the SearchCursor 
    fld_name_list=cursor.fields #Defining the fields within the "fc" dataset
    search_field="Site_NGUID" #Defining the field that I am interested in
    indx=fld_name_list.index(search_field) # Obtaining the index number from the tuple of field names. This is instead of using fld_name_list[6]
    nguid=[]
    global MaxNGUID 
    MaxNGUID = 0
    p=0
    if search_field in fld_name_list:
        #print('Yes, ' + search_field + ' is in the table')
        for row in cursor:
            #print(row[indx])
            tempNGUID = row[indx]
            if tempNGUID is None:
                print('Value is None')
                p +=1
            elif tempNGUID == '':
                print('Value is None')
                p +=1
            else:
                nguidNumber=int(row[indx][12:])
                #print(str(nguidNumber) + "  is an interger")
                if MaxNGUID < nguidNumber:
                    MaxNGUID = nguidNumber
                    #print(nguidNumber)
                #print(MaxNGUID)
    else:
        print('The field that you are looking for is not in the data.')
    return MaxNGUID

MaxNGUID = findMaxNGUID(wrkspc, fc)
print('\n\n\tMax NGUID is:   ' + str(MaxNGUID) + "\n")



def SelectUpdateRecordsWithoutNGUID():
    arcpy.management.SelectLayerByAttribute(fc, 'CLEAR_SELECTION')
    arcpy.management.SelectLayerByAttribute(fc, "NEW_SELECTION", '''Site_NGUID IS NULL''', None) # This stopped working after an update.
    arcpy.management.SelectLayerByAttribute(fc, 'ADD_TO_SELECTION',"Site_NGUID = ''",None)
    count = arcpy.management.GetCount(fc)
    print('The number of records without an NGUID is:  ' + str(count) + '\n\n')
    # To add in the future: https://support.esri.com/en/technical-article/000023601

SelectUpdateRecordsWithoutNGUID()


recImport = "autoIncrement(" + str(MaxNGUID) + ")"
arcpy.management.CalculateField(fc, "Site_NGUID", recImport, "PYTHON3", '''rec = MaxNGUID
def autoIncrement(MaxNGUID):
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
    arcpy.management.SelectLayerByAttribute(fc, 'CLEAR_SELECTION') 
ClearSelectedRecords()

SelectSendLetterRecords()

## Create Export location/folder    ## Create the folder for the files to be saved in
def CreateTodaysAddressFolder():
    '''Creates folder inside of MailingAppendLetters on the desktop and includes the date and time the folder was created'''
    import os
    folderDate = str(datetime.datetime.today().strftime('%m_%d_%Y_Time_%H_%M')).split()[0]
    folderUsed = MailingLettersFolder + os.path.sep + str(folderDate) + '-Address_Data_Letters'
    workingDirectory = os.mkdir(folderUsed)
    print(folderDate)
    print('Folder Created at: \n\t' +folderUsed)
    #time.sleep(5)
    dataFolderCreate = os.mkdir(str(folderUsed) + os.path.sep + 'Data')
    dataFolder = str(folderUsed) + os.path.sep + 'Data'
    YCDirectory = os.mkdir(dataFolder + os.path.sep + 'Yellowstone_Club')
    NewDirectory = os.mkdir(dataFolder + os.path.sep + 'New_Addresses')
    return folderDate, folderUsed, dataFolder, MailingLettersFolder; # returned as a tuple

folderDate, folderUsed, dataFolder, MailingLettersFolder = CreateTodaysAddressFolder()
print("Folder Date: \t\t" +folderDate + "\nMain Folder: \t\t" + folderUsed + "\nData Folder: \t\t" + dataFolder)

## Export selected features
def ExportFeaturesExcelAndTable2(fc,dataFolder,folderDate,MailingLettersFolder,FileName):
    # Join Parcels to Structures in order to export with all necessary data
    try:
        arcpy.management.RemoveJoin(fc, "L0Parcels")
    except:
        print('No join present')
    arcpy.management.AddJoin(fc, 'ParcelID', parcels, 'PARCELID', 'KEEP_ALL')
    
    # To add in the future: https://support.esri.com/en/technical-article/000023601
    ## Export Shapefile
    import os
    BasePath = MailingLettersFolder + os.path.sep + folderDate + '-Address_Data_Letters'    
    OutputFileName = FileName + '__' + folderDate
    ##Create shapefile
    if os.path.exists(dataFolder + os.path.sep + 'SiteStructureAddressPoints.shp'):
        print('shape file already exists')
    else:
        pass
    if FileName == 'Yellowstone_Club':
        arcpy.conversion.FeatureClassToShapefile(fc,dataFolder + os.path.sep + 'Yellowstone_Club')
    else:
        arcpy.conversion.FeatureClassToShapefile(fc,dataFolder + os.path.sep + 'New_Addresses')
    ##Create CSV file
    arcpy.conversion.TableToTable(fc,BasePath,OutputFileName + '.csv')
    ##Create Excel file
    arcpy.conversion.TableToExcel(fc, BasePath + os.path.sep + OutputFileName + '.xls')
    
    mergeFile = MailingLettersFolder + os.path.sep + FileName + '.xls'
    if os.path.exists(mergeFile):
        os.remove(mergeFile)
    else:
        print('mergeFile did not exist')
    arcpy.conversion.TableToExcel(fc,mergeFile)
    

SelectSendLetterRecords()

FileName =    'New_Addresses'
ExportFeaturesExcelAndTable2(fc,dataFolder,folderDate,MailingLettersFolder,FileName)
print('\n\n\t' + FileName + ' First Export Complete')
## Need to create area specific PDF file generation (Postal codes, YC, Incorporated Areas, etc.)

# Yellowstone Club
SelectionYC = r"Nbrhd_Comm = 'Yellowstone Club' And SendLetter = 1"
#arcpy.management.SelectLayerByAttribute(fc, "NEW_SELECTION", SelectionYC, None)
arcpy.management.SelectLayerByAttribute(fc, "NEW_SELECTION", "Nbrhd_Comm = 'Yellowstone Club' And SendLetter = 1", None)
countYC = str(arcpy.management.GetCount(fc))
if int(countYC) >0:
    FileName = 'Yellowstone_Club'
    ExportFeaturesExcelAndTable2(fc,dataFolder,folderDate,MailingLettersFolder,FileName)
    print('\n\n\t' + FileName + ' First Export Complete')
else:
    print('No YC structures selected')


SelectSendLetterRecords()
arcpy.management.RemoveJoin(fc, "L0Parcels")
print('Join removed')


def MailMerge():
    WordMergeDoc = r"C:\Users\TLuksha\Desktop\Mail Merge Letter 2.docx" # From Line 30
    ExcelSourceName = 
    import os
    import win32com.client as win32 # pip install pywin32
    
    os.startfile(WordMergeDoc)
    

#ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
#ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
#ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ

# Fix line 217
## May have to remove the table from the map: https://pro.arcgis.com/en/pro-app/latest/arcpy/mapping/map-class.htm

#ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
#ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
#ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ


## This portion of the script will update the "Send Letter" field and the "Letter Sent" date field.

dateField = "LetterSent"
count = arcpy.management.GetCount(fc)
if count != 0:
    with arcpy.da.UpdateCursor(fc, ["LetterSent"]) as rows:
        for row in rows:
            rows.updateRow([datetime.date.today()])
else:
    print('You must have a selection made for the script to run')    

arcpy.management.CalculateField(fc, "SendLetter", "'0'", "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")


'''
#ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
## Cannot use "  input()  " in ArcPro
#ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
def answerQuestion(question):
    while True:
        askQuestion = input(question + " Answer Y or N \n").upper()
        if askQuestion in ["Y","N","YES","NO"]:
            break
        print("Sorry, I didn't understand that.")
    
    if askQuestion == "Y" or askQuestion == "YES": 
        print("Thank you for selecting  Yes \nWe will process your request\n")
        return "Y"
    else:
        print("You have selected  No \nWe will NOT process this portion\n")
        return "N"

question = r"Would you like to update the Letter Sent date? "
updateLetterSentField = answerQuestion(question)

updateLetterSentField = 'N'
if updateLetterSentField = 'Y':
    # Still need to clean this portion up.
    ## Update LetterSent field
    SelectSendLetterRecords()
    today = datetime.datetime.today() # Still need to clean this portion up.
    arcpy.management.CalculateField(fc, "LetterSent", today, "PYTHON3", '', "TEXT") # Still need to clean this portion up.
    # Still need to clean this portion up.
    ## Alternate version:
    arcpy.management.CalculateField(fc, "LetterSent", folderDate[:10])
else:
    pass


#def SelectSendLetterRecords():
    #arcpy.management.SelectLayerByAttribute(fc, 'CLEAR_SELECTION')
    #sendLetterqry = '"SendLetter" = 1'
    #arcpy.management.SelectLayerByAttribute(fc, 'NEW_SELECTION', sendLetterqry)
'''

arcpy.management.CalculateField(fc, "Label", "UpdateLabel(!Add_Number!,!AddNum_Suf!,!LSt_PreType!,!LSt_PreDir!,!LSt_Name!,!LSt_Type!,!LSt_PosDir!,!Unit!)", "PYTHON3", """def UpdateLabel(Add_Number, AddNum_Suf, LSt_PreType, LSt_PreDir, LSt_Name, LSt_Type, LSt_PosDir,Unit):
    if Unit is None:
        returnValue = " ".join([str(i) for i in [ Add_Number, AddNum_Suf, LSt_PreType, LSt_PreDir, LSt_Name, LSt_Type, LSt_PosDir] if i]).strip().replace('   ',' ').replace('  ',' ')
    else:
        returnValue = " ".join([str(i) for i in [ Add_Number, AddNum_Suf, LSt_PreType, LSt_PreDir, LSt_Name, LSt_Type, LSt_PosDir, "UNIT", Unit] if i]).strip().replace('   ',' ').replace('  ',' ')
    returnValue = returnValue.replace('  ',' ')
    return returnValue""", "TEXT", "NO_ENFORCE_DOMAINS")
