import arcpy
from arcpy.sa import *
import os

arcpy.CheckOutExtension("Spatial")


def dbfToXls(inTable, outTable):
    return arcpy.TableToExcel_conversion(inTable, outTable)


def reclassifyRasterByThreshold(inRaster, threshold, outRasterPath):
    inRaster = arcpy.Raster(inRaster)
    outRaster = Con(inRaster < threshold, 0, inRaster)
    outRaster.save(outRasterPath)


def execExtractByMask(inRaster, inMaskData, outRaster):
    outExtractByMask = ExtractByMask(inRaster, inMaskData)
    outExtractByMask.save(outRaster)


def zonalRasterByFeature(inRaster, inFeature, zoneField, outTable, statisticsType):
    outZSaT = ZonalStatisticsAsTable(inFeature, zoneField, inRaster,
                                     outTable, ignore_nodata="NODATA", statistics_type=statisticsType)


def featureToRaster(inFeature, field, cellSize, outRaster):
    arcpy.FeatureToRaster_conversion(inFeature, field, outRaster, cellSize)


def estimatingStock(inLightRaster, inZoneEffectsRaster, slope, intercept, timeEffects, outStockRasterPath):
    light = arcpy.Raster(inLightRaster)
    zoneEffects = arcpy.Raster(inZoneEffectsRaster)
    outStockRaster = Exp(slope * Ln(light) + intercept + timeEffects + zoneEffects)
    outStockRaster.save(outStockRasterPath)
    print "success."

def estimateStockSimpleRegression(inLightRaster, slope, intercept, outStockRasterPath):
    light = arcpy.Raster(inLightRaster)
    outStockRaster = Exp(slope * Ln(light) + intercept)
    outStockRaster.save(outStockRasterPath)
    print "success."




