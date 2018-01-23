import arcpy
from arcpy import env
from arcpy.sa import *
import os
arcpy.CheckOutExtension("Spatial")

def execExtractByMask(inRaster, inMaskData, outRaster):
    outExtractByMask = ExtractByMask(inRaster, inMaskData)
    outExtractByMask.save(outRaster)

if __name__ == "__main__":
    nightttimeLightRasters = r"G:\Nighttime Light Data\Open Calibration Projected"
    inRasters = filter(lambda r: r[-3:] == "tif", os.listdir(nightttimeLightRasters))
    continentsFeatures = r"G:\Stock Estimation Study\Continents"
    inMasks = filter(lambda r: r[-3:] == "shp", os.listdir(continentsFeatures))
    continents = map(lambda c: c[:-4], inMasks)
    outputDir = r"G:\Nighttime Light Data\Continents"
    for inMask in inMasks:
        if os.path.exists(outputDir + "\\" + inMask.split(".")[0]) is not True:
            os.mkdir(outputDir + "\\" + inMask.split(".")[0])
    inRasterPaths = map(lambda a: nightttimeLightRasters + "\\" + a, inRasters)
    inMaskPaths = map(lambda a: continentsFeatures + "\\" + a, inMasks)
    for i in range(len(inRasterPaths)):
        for j in range(len(inMaskPaths)):
            outRaster = outputDir + "\\" + continents[j] + "\\" + continents[j] + "_" + inRasters[i][:-9]
            # execExtractByMask(inRasterPaths[i], inMaskPaths[j], )
            print inRasterPaths[i], inMaskPaths[j], outRaster
            execExtractByMask(inRasterPaths[i], inMaskPaths[j], outRaster)
            print "break point"




