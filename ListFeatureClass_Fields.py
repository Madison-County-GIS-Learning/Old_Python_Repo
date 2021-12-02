## List fields in a feature class or shapefile
## Creates a comma seperated value list of attributes
## https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/listfields.htm

fields = arcpy.ListFields("Standard Working Data\\Online_MC_Layers\\SiteStructureAddressPoints")
for field in fields:
    print("{0}, is a type of ,{1}, with a length of ,{2}"
          .format(field.name, field.type, field.length))