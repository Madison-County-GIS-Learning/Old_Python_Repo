def SelectSendLetterRecords(query = '"SendLetter" = 1'):
    #query = '"SendLetter" = 1'
    arcpy.management.SelectLayerByAttribute(fc, 'NEW_SELECTION', query)
    count = arcpy.management.GetCount(fc)
    print('The number of  SendLetter  records selected is:  ' + str(count) + '\n')    
    # To add in the future: https://support.esri.com/en/technical-article/000023601