from ArcPyTools import *
import os

if __name__ == "__main__":
    inFeature = r"G:\Stock Estimation Study\ADM0\admo_moll_cement_rates.shp"
    fields = [
        "r21992",
        "r21993",
        "r21994",
        "r21995",
        "r21996",
        "r21997",
        "r21998",
        "r21999",
        "r22000",
        "r22001",
        "r22002",
        "r22003",
        "r22004",
        "r22005",
        "r22006",
        "r22007",
        "r22008",
        "r22009",
    ]
    outRastersDir = r"L:\RatesRasters"
    for field in fields:
        outRaster = outRastersDir + "\\" + "cement_rates_%s.tif" % field
        featureToRaster(inFeature, field, 1000, outRaster)
        print field