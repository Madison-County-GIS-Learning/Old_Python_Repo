## Weed Board Files are working
import os
import shutil
import requests
import urllib.request
from datetime import datetime, timedelta
# This is for python3

initialStartTime = datetime.now() 

label = datetime.now().strftime("%Y-%m-%d_Time-%H-%M")    #Creates the timestamp for the label
currentTime = str(datetime.now())  
date = str(datetime.now())[:10]    
hour = str(datetime.now())[11:13]    
minute = str(datetime.now())[14:16]    
second = str(datetime.now())[16:18]
print(currentTime)
print('Initial Start Time is:  \t\t\t\t\t\t\t\t\t' + str(initialStartTime))
estCompletedTime = initialStartTime + timedelta(minutes = 6)  #    datetime.timedelta(minutes = 10)
print('Expected completion time is:   \t\t\t\t\t\t\t' + str(estCompletedTime))
print('Folder Label is:  ' + label)


weedBoardVariables = []
## Files for WeedBoard:

##File format = [FTP_Site_Address (informal without r'ftp://' or 'ftp://'), FTP_Directory_Path, FTP_File_To_Download]
##  Output_Save_Path is passed each time
#Output_Save_Path = 'C:/Users/TLuksha/Desktop/FTP_Test'

# Montana Blue and Red Ribbon Streams: https://databasin.org/datasets/

#GWIC_Wells
GWICwells_Site = 'ftp.geoinfo.msl.mt.gov'
GWICwells_Directory_Path = '/Data/Spatial/NonMSDI/Wells/'
GWICwells_Download = 'GWIC_wells.gdb.zip'
GWICwells = [GWICwells_Site, GWICwells_Directory_Path, GWICwells_Download]

#NHD Dataset
NHD_Site = 'ftp.geoinfo.msl.mt.gov'
NHD_Directory_Path = '/Data/Spatial/MSDI/Hydrography/' 
NHD_Download = 'NHDH_MT_Shape_20191029.zip'
NHD = [NHD_Site,  NHD_Directory_Path, NHD_Download]

#NHD Dataset Layerfiles
NHDLayer_Site = 'ftp.geoinfo.msl.mt.gov'
NHDLayer_Directory_Path = '/Data/Spatial/MSDI/Hydrography/'
NHDLayer_Download = 'NHDLayerfiles.zip'
NHDLayer = [NHDLayer_Site, NHDLayer_Directory_Path, NHDLayer_Download]

#Conservation Easements
ConservationEasements_Site = 'ftp.geoinfo.msl.mt.gov'
ConservationEasements_Directory_Path = '/Data/Spatial/MSDI/Cadastral/ConservationEasements/'
ConservationEasements_Download = 'MTConservationEasements_SHP.zip'
ConservationEasements = [ConservationEasements_Site, ConservationEasements_Directory_Path, ConservationEasements_Download]

#Parcels 
Parcels_Site = 'ftp.geoinfo.msl.mt.gov'
Parcels_Directory_Path = '/Data/Spatial/MSDI/Cadastral/Parcels/Madison/'
Parcels_Download = 'Madison_SHP.zip'
Parcels = [Parcels_Site, Parcels_Directory_Path, Parcels_Download]

#PLSS
PLSS_Site = 'ftp.geoinfo.msl.mt.gov'
PLSS_Directory_Path = '/Data/Spatial/MSDI/Cadastral/PLSS/'
PLSS_Download = 'CadNSDI_MT_2018_11_20_Shapefiles.zip'
PLSS = [PLSS_Site, PLSS_Directory_Path, PLSS_Download]

#Public Lands
PublicLands_Site = 'ftp.geoinfo.msl.mt.gov'
PublicLands_Directory_Path = '/Data/Spatial/MSDI/Cadastral/PublicLands/'
PublicLands_Download = 'MTPublicLands_GDB.zip'
PublicLands = [PublicLands_Site, PublicLands_Directory_Path, PublicLands_Download]

#Public Lands Layerfiles
PublicLandLayer_Site = 'ftp.geoinfo.msl.mt.gov'
PublicLandLayer_Directory_Path = '/Data/Spatial/MSDI/Cadastral/PublicLands/'
PublicLandLayer_Download = 'PublicLands.lyr'
PublicLandLayer = [PublicLandLayer_Site, PublicLandLayer_Directory_Path, PublicLandLayer_Download]

#Waterways
WaterWays_Site = 'ftp.geoinfo.msl.mt.gov'
WaterWays_Directory_Path = '/Data/Spatial/NonMSDI/Shapefiles/'
WaterWays_Download = 'Stream_Lake_Generalized.zip'
WaterWays = [WaterWays_Site, WaterWays_Directory_Path, WaterWays_Download]

#NAIP
NAIP_Site = 'ftp.geoinfo.msl.mt.gov'
NAIP_Directory_Path = '/Data/Spatial/MSDI/Imagery/2019_NAIP/UTM_County_Mosaics/'
NAIP_Download = 'Madison.sid'
NAIP = [NAIP_Site, NAIP_Directory_Path, NAIP_Download]

##NOT FTP Use another Method
#Commissioner Districts
CommissionerDistricts = r'E:\GIS\DailyData\CommissionerDistricts'
#Incorporated Areas
IncorporatedAreas = r'E:\GIS\DailyData\IncorporatedCommunities'
#RoadsStructureRoutes
RoadsStructuresRoutes = r'E:\GIS\DailyData\Road_Struct'

##Structures
#Structures = r'G:\GIS\DailyData\Road_Struct\2020_Structures.shp'
##Roads
#Roads = r'G:\GIS\DailyData\Road_Struct\2020_Roads.shp'
##Routes
#Routes = r'G:\GIS\DailyData\Road_Struct\Routes.shp'
#All Local Files
allLocalFiles = [CommissionerDistricts, IncorporatedAreas, RoadsStructuresRoutes]

##NOT FTP Use another Method
#Mile Reference Markers
ReferenceMarkers = r'https://opendata.arcgis.com/datasets/31791c42bb3e4f1fba1ef34336373dec_0.zip?outSR=%7B%22latestWkid%22%3A3857%2C%22wkid%22%3A102100%7D'

## IGNORE -- Parcels and PLSS
## IGNORE -- ftp://ftp.geoinfo.msl.mt.gov', '/Data/Spatial/MSDI/Cadastral/Parcels/Madison/Madison_GDB.zip


def notificationSound(duration, text):
    import winsound, time, os    #code from https://realpython.com/playing-and-recording-sound-python/#playing-audio-files
    ##Play wave file for notification # Additional information: https://www.geeksforgeeks.org/morse-code-translator-python/    OR    https://www.tutorialspoint.com/morse-code-translator-in-python
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-' }
    text = text.upper()
    for i in text:
        print(i + '  ' + MORSE_CODE_DICT[i])
        HzHigh = 1000 #toneHigh
        HzLow = 800 #toneLow
        rate = duration
        for letter in MORSE_CODE_DICT[i]:
            if letter == '.':
                rate = 100
                Hz = HzLow
            elif letter == '-':
                rate = 200
                Hz = HzHigh
            winsound.Beep(Hz,rate)
            time.sleep(0.5)
            
    #filename = r'C:\Windows\Media\Ring05.wav'
    #winsound.PlaySound(filename, winsound.SND_FILENAME)
    #rate = 400
    #count = 0
    #for i in text:
        #count = count +1
        #print(count)
        #print(i)
    #HzHigh = 1000 #toneHigh
    #HzLow = 900 #toneLow
    #for i in range(1):
        #winsound.Beep(HzHigh, rate)  # Beep at 1000 Hz for 300 ms
        #time.sleep(0.1)
        #winsound.Beep(HzHigh, rate)  # Beep at 1000 Hz for 300 ms
        #winsound.Beep(HzHigh, rate)  # Beep at 1000 Hz for 300 ms
        #winsound.Beep(HzHigh, rate)  # Beep at 1000 Hz for 300 ms
        #time.sleep(0.1)
        #winsound.Beep(HzHigh, rate)  # Beep at 1000 Hz for 300 ms
        #winsound.Beep(HzHigh, rate)  # Beep at 1000 Hz for 300 ms
        #time.sleep(0.1)
        #winsound.Beep(HzHigh, rate)  # Beep at 1000 Hz for 300 ms
        #winsound.Beep(HzHigh, rate)  # Beep at 1000 Hz for 300 ms
        #time.sleep(0.1)
        #winsound.Beep(HzHigh, rate)  # Beep at 1000 Hz for 300 ms
        #winsound.Beep(HzLow, int(rate/4))  # Beep at 1000 Hz for 90 ms
        #winsound.Beep(HzHigh, rate)  # Beep at 1000 Hz for 300 ms
        #winsound.Beep(HzHigh, rate)  # Beep at 1000 Hz for 300 ms
    #time.sleep(30)

## Placeholder portion of the script.

def TimeCalculation(initialStartTime):    ## This is the time tracking code function.
    # printing initial_date  
    runTime = datetime.now() - initialStartTime
    #print('Process Run Time is:  ' + str(runTime))
    return runTime 

## Placeholder portion of the script.

def downloadFromFTP(itemToSave, Output_Save_Path):
    import ftplib, os
    with ftplib.FTP(itemToSave[0]) as ftp:
        ftp.login()
        print(ftp.getwelcome())
        ftp.cwd(itemToSave[1])
        print(ftp)
        print('Current Directory: ', ftp.pwd())
        #ftp.dir()
        os.chdir(Output_Save_Path) #    Changes the working directory for the download 
        ftp.retrbinary('RETR '+ itemToSave[2], open(itemToSave[2], 'wb').write)
        extractZipFile(itemToSave,str(itemToSave[2])[:-4])
        evaluator = str(itemToSave[2])[-4:] 
        if evaluator == '.zip':
            os.remove(itemToSave[2])
            print('Line 119 is handling: ', itemToSave[2])
        print('File saved \n \n \nEvaluator is equal to: ', evaluator)
        ftp.quit()
## Placeholder portion of the script.

def downloadFromHTTPS(Output_Save_Path):
    url = r'https://opendata.arcgis.com/datasets/31791c42bb3e4f1fba1ef34336373dec_0.zip?outSR=%7B%22latestWkid%22%3A3857%2C%22wkid%22%3A102100%7D'
    os.chdir(Output_Save_Path) #    Changes the working directory for the download 
    r = requests.get(url, allow_redirects=True)
    print('Line 80 contains the variable "r" and its value is set to:  ', r)
    print(r.headers.get('content-type'))
    open('Montana_Reference_Markers-shp.zip', 'wb').write(r.content)
    extractZipFile('Montana_Reference_Markers-shp.zip','Montana_Reference_Markers-shp')
    from zipfile import ZipFile 
    try:
        with ZipFile('Montana_Reference_Markers-shp.zip', 'r') as zip: 
            print('Extracting the following files now...')
            print(zip.namelist())
            FGDB = zip.namelist()[0]
            zip.extractall('Montana_Reference_Markers-shp')
            print('HTTP extraction is Done!\n') 
            
    except Exception as e:
        print(e)
        pass
    os.remove('Montana_Reference_Markers-shp.zip')

## Placeholder portion of the script.

def extractZipFile(input_file_name, output_file_name):
    # importing required modules 
    from zipfile import ZipFile 
    try:
        with ZipFile(input_file_name[2], 'r') as zip: 
            print('Extracting the following files now...')
            print(zip.namelist())
            FGDB = zip.namelist()[0]
            zip.extractall(output_file_name)
            print(output_file_name + '  is Done!\n') 
    except Exception as e:
        print(e)
        pass
    

## Placeholder portion of the script.

def copyLocalFiles(allLocalFiles, Output_Save_Path):
    try:
        for i in allLocalFiles:
            shutil.copytree(i,Output_Save_Path+i[6:])
    except Exception as e:
        print(e)

## Placeholder portion of the script.


print('Line 219 -Script started')

## Commented for speed sake -- YOU WILL NEED THE FOLLOWING FOR THE FINAL SCRIPT


######################################################################################################################
##                                                                           File selection is below this point                                                                                ##
######################################################################################################################

##    Weed Board Files
WeedBoardVariables = [GWICwells, NHD, NHDLayer, ConservationEasements, Parcels, PLSS, PublicLands, PublicLandLayer, WaterWays] #    , CommissionerDistricts, IncorporatedAreas, Structures,  Roads, Routes] #ReferenceMarkers, NAIP] 
WeedBoard_Output_Save_Path = 'C:/Users/TLuksha/Desktop/' + label + 'Weed-Board-Update'
#makeDirectory = os.mkdir(WeedBoard_Output_Save_Path)

##    Dispatch Files
DispatchVariables = [Parcels, PLSS, PublicLands, PublicLandLayer, WaterWays]
Dispatch_Output_Save_Path = 'C:/Users/TLuksha/Desktop/' + label + '-Dispatch-Update'

#group = input('Please enter a "D" for a Dispatch download: D \nPlease enter a "W" for a Weed Board download: W\n\n\t...')
#if group == 'D':
    #Output_Variables = DispatchVariables
    #Output_Save_Path = Dispatch_Output_Save_Path
#elif group == 'W':
    #Output_Variables = WeedBoardVariables
    #Output_Save_Path = WeedBoard_Output_Save_Path
#else:
    #pass


Output_Variables = WeedBoardVariables # DispatchVariables #    WeedBoardVariables
Output_Save_Path = WeedBoard_Output_Save_Path # Dispatch_Output_Save_Path #    WeedBoard_Output_Save_Path
print('Output_Variables is equal to:  '+ str(Output_Variables) +'\nOutput_Save_Path is equal to:  ' + Output_Save_Path)

#def DataDownloader(Output_Variables, Output_Save_Path):
if not os.path.exists(Output_Save_Path):
    os.mkdir(Output_Save_Path)
    print('Folder created at', Output_Save_Path)

for i in Output_Variables:
    downloadFromFTP(i, Output_Save_Path)
    print('FTP download Completed: ', i)
    print('Saved to: ', Output_Save_Path)

downloadFromHTTPS(Output_Save_Path)  #
print('HTTPS download Completed.')
print('Saved to: ', Output_Save_Path)

copyLocalFiles(allLocalFiles, Output_Save_Path)

print('All files Complete')

## Placeholder portion of the script.

print('File Transfer Protocol Completed')