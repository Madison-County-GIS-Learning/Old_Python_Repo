import arcpy
arcpy.management.CalculateField(r"Online_MC_Layers\SiteStructureAddressPoints", "Site_NGUID", "autoIncrement()", "PYTHON3", r'rec = 9165
def autoIncrement():
    arcpy.AddMessage("The process is starting.")
    global rec
    pStart = 999999
    pInterval = 1
    if (rec == 0):
        arcpy.AddMessage("Please enter the previous NGUID number value")
        rec = pStart
    else:
        arcpy.AddMessage("Good run. rec = " + str(rec))
        rec = rec + pInterval
    return "STR.MADISON." + str(rec)
', "TEXT")
