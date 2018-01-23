from ArcPyTools import *
from arcpy.sa import *
import os

if __name__ == "__main__":
    inFeature = r"G:\Stock Estimation Study\ADM0\adm0_moll_rates_simple_reg.shp"
    outRasterDir = r"M:\CorrectedSimpleRegEstimatedStock"
    fields = [
        "RATE1992",
        "RATE1993",
        "RATE1994",
        "RATE1995",
        "RATE1996",
        "RATE1997",
        "RATE1998",
        "RATE1999",
        "RATE2000",
        "RATE2001",
        "RATE2002",
        "RATE2003",
        "RATE2004",
        "RATE2005",
        "RATE2006",
        "RATE2007",
        "RATE2008",
    ]

    for field in fields:
        outRaster = outRasterDir + "\\steel_%s.tif" % field
        cellSize = 1000
        featureToRaster(inFeature, field, cellSize, outRaster)
        print field