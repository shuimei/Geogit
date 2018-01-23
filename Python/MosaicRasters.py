import os
import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")


def mosaicRaster(inRasters, outDir, outRaster):
    cat = lambda a1, a2: a1 + ';' + a2
    arcpy.MosaicToNewRaster_management(reduce(cat, inRasters), outDir, outRaster,
                                       pixel_type="32_BIT_FLOAT", number_of_bands="1")


def listMosaicRasters(rastersDir, year):
    continents = os.listdir(rastersDir)
    rasters = []
    for continent in continents:
        currDir = rastersDir + "\\" + continent
        continentRasters = filter(lambda a: a[-3:] == "tif", os.listdir(currDir))
        continentRasters = map(lambda c: rastersDir + "\\" + continent + "\\" + c, continentRasters)
        rasters.extend(filter(lambda a: str(year) in a, continentRasters))
    return rasters


if __name__ == "__main__":
    rastersDir = r"K:\ThresholdExtractionRasters_dot4"
    years = range(1993, 2013)
    for year in years:
        inRasters = listMosaicRasters(rastersDir, year)
        outDir = r"K:\ThresholdExtractionRasters_dot4_mosaic"
        outRaster = r"dot4_c2_%d.tif" % year
        mosaicRaster(inRasters, outDir, outRaster)