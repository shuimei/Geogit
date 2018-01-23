from ArcPyTools import *
from arcpy.sa import *
import os

if __name__ == "__main__":
    inLightRastersDir = r"M:\ThresholdExtractionRasters_dot4_mosaic"
    outStockRasterDir = r"M:\SimpleRegEstimatedStock"
    slopes = [
        0.984946,
        0.9957774,
        0.9503118,
        0.9764011,
        0.9557009,
        0.9770187,
        0.9615916,
        1.007777,
        1.003466,
        0.9750555,
        1.01174,
        0.9859843,
        1.012774,
        0.9633563,
        0.9470342,
        0.9509268,
        0.968425,
    ]
    intercepts = [
        4.600453,
        4.227275,
        4.23389,
        4.178249,
        4.309152,
        4.144944,
        4.203146,
        4.273805,
        4.304887,
        4.287448,
        4.224602,
        4.358395,
        4.370546,
        4.36581,
        4.450392,
        4.60036,
        4.485179,
    ]
    for year in range(1993, 2009):
        inLightRaster = inLightRastersDir + r"\dot4_c2_%d.tif" % year
        outStockRasterPath = outStockRasterDir + r"\dot4_steel_%d_simple_reg.tif" % year
        estimateStockSimpleRegression(inLightRaster, slopes[year - 1992], intercepts[year - 1992], outStockRasterPath)
        print year
