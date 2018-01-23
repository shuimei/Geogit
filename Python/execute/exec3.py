from ArcPyTools import *
from arcpy.sa import *
import os

if __name__ == "__main__":
    stocksRastersDir = r"M:\SimpleRegEstimatedStock"
    ratesRastersDir = r"M:\RatesSimpleRegEstimatedStock"
    steelRasters = filter(lambda a: (a[-3:] == "tif") and ("steel" in a), os.listdir(stocksRastersDir))
    steelRasters = [stocksRastersDir + "\\" + steelRaster for steelRaster in steelRasters]
    ratesRasters = filter(lambda a: (a[-3:] == "tif") and ("steel" in a), [ratesRastersDir + "\\" + ratesRaster for ratesRaster in os.listdir(ratesRastersDir)])
    for i, j in zip(steelRasters, ratesRasters):
        stock = arcpy.Raster(i)
        rate = arcpy.Raster(j)
        out = Times(stock, rate)
        out.save(r"M:\CorrectedSimpleRegEstimatedStock\corrected_%s" % os.path.split(i)[1])
        print r"M:\CorrectedSimpleRegEstimatedStock\corrected_%s" % os.path.split(i)[1]