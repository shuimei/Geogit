import arcpy
from arcpy.sa import *
import pickle
import os

arcpy.CheckOutExtension("Spatial")


def reclassifyRasterByThreshold(inRaster, threshold, outRasterPath):
    inRaster = arcpy.Raster(inRaster)
    outRaster = Con(inRaster < threshold, 0, inRaster)
    outRaster.save(outRasterPath)


def main():
    continentsDir = r"G:\Nighttime Light Data\Continents"
    continents = os.listdir(continentsDir)
    outRastersDir = r"K:\ThresholdExtractionRasters_dot4"
    for continent in continents:
        inRastersDir = r"G:\Nighttime Light Data\Continents\%s" % continent
        if os.path.exists(outRastersDir + "\\" + continent) is not True:
            os.mkdir(outRastersDir + "\\" + continent)
        thresholdDir = r"G:\Stock Estimation Study\Threshold\dot4"
        inThresholds = filter(lambda a: continent in a, os.listdir(thresholdDir))
        inRasters = filter(lambda a: a[-3:] == "tif", os.listdir(inRastersDir))
        for inRaster, threshold in zip(inRasters, inThresholds):
            inRasterPath = inRastersDir + "\\" + inRaster
            thresholdPath = thresholdDir + "\\" + threshold
            threshold = pickle.load(open(thresholdPath, "r"))[2]
            print inRaster, "threshold = %f" % threshold
            outRastersPath = outRastersDir + "\\" + continent +"\\dot4_" + inRaster
            reclassifyRasterByThreshold(inRasterPath, threshold, outRastersPath)
            # print inRasterPath, thresholdPath, outRastersPath



if __name__ == "__main__":
    main()
