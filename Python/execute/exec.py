from ArcPyTools import *
import os

if __name__ == "__main__":
    #     inRastersDir = r"L:\EstimatedStock"
    #     inRasters = filter(lambda a: a[-3:] == "tif", [inRastersDir + "\\" + i for i in os.listdir(inRastersDir)])
    #     inFeature = r"I:\DATA\Vector Data\ADM0\admo_moll_rates.shp"
    #     zoneField = "ISO"
    #     outTablesDir = r"L:\EstimatedStockZonalTables"
    #     statisticsType = "MEAN"
    #     for inRaster in inRasters:
    #         outTable = outTablesDir + "\\" + os.path.split(inRaster)[1][:-3] + "dbf"
    #         zonalRasterByFeature(inRaster, inFeature, zoneField, outTable, statisticsType)
    inLightRastersDir = r"L:\ThresholdExtractionRasters_dot4_mosaic"

    inZoneEffectsRaster = r"L:\ZoneEffectsRasters\al_zone_effects.tif"
    slope = 0.4733397
    intercept = -1.840654
    timeEffectsDict = {
        1992: 0,
        1993: -0.129406,
        1994: -0.1176847,
        1995: -0.0752216,
        1996: -0.0365111,
        1997: -0.0241225,
        1998: 0.036201,
        1999: 0.053782,
        2000: 0.1220358,
        2001: 0.1838493,
        2002: 0.2442278,
        2003: 0.3182977,
        2004: 0.4040333,
        2005: 0.490974,
        2006: 0.5754624,
        2007: 0.6545021,
        2008: 0.6790142,
        2009: 0.822349,
        2010: 0.75393,
    }
    outStockRasterDir = r"L:\EstimatedStock"
    for year in range(1992, 2011):
        inLightRaster = inLightRastersDir + r"\dot4_c2_%d.tif" % year
        timeEffects = timeEffectsDict[year]
        print timeEffects
        outStockRasterPath = outStockRasterDir + r"\dot4_al_%d.tif" % year
        estimatingStock(inLightRaster, inZoneEffectsRaster, slope, intercept, timeEffects, outStockRasterPath)
        print year
