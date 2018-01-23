import arcpy
import os
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

def zonalRasterByFeature(inRaster, inFeature, zoneField, outTable, statisticsType):
    outZSaT = ZonalStatisticsAsTable(inFeature, zoneField, inRaster,
                                     outTable, ignore_nodata="NODATA", statistics_type=statisticsType)

if __name__ == "__main__":
    inRasterDir = r"K:\ThresholdExtractionRasters_dot4_mosaic"
    inRasters = filter(lambda a: a[-3:] == "tif", os.listdir(inRasterDir))
    for inRaster in inRasters:
        inFeature = r"I:\DATA\Vector Data\ADM0\admo_moll.shp"
        zoneField = "ISO"
        outTable = r"K:\ThresholdExtractionZonalTables\%s.dbf" % inRaster[:-4]
        print outTable
        statisticsType = "SUM"
        inRaster = inRasterDir + "\\" + inRaster
        zonalRasterByFeature(inRaster, inFeature, zoneField, outTable, statisticsType)