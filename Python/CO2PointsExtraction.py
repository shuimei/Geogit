from osgeo import ogr
import os
os.chdir(r"J:\EDGAR\v42_CO2_org_short-cycle_C_2008-1970_TOT_txt")
fileName = "v42_CO2_org_short-cycle_C_1970_TOT.txt"
co2points = open(fileName, "r")
year = int(fileName.split("_")[5])
for i in xrange(4):
	co2points.next()
lat, lng, co2 = map(float,co2points.next().rstrip("\n").split(";"))
outSHPfn = "../test.shp"

shpDriver = ogr.GetDriverByName("ESRI Shapefile")
if os.path.exists(outSHPfn):
	shpDriver.DeleteDataSource(outSHPfn)
outDataSource = shpDriver.CreateDataSource(outSHPfn)
outLayer = outDataSource.CreateLayer(outSHPfn, geom_type=ogr.wkbPoint)

point = ogr.Geometry(ogr.wkbPoint)
point.AddPoint(lng, lat)

yearField = ogr.FieldDefn("year",ogr.OFTInteger)
co2Field = ogr.FieldDefn("co2_emission", ogr.OFTReal)
outLayer.CreateField(yearField)
outLayer.CreateField(co2Field)

featureDefn = outLayer.GetLayerDefn()
outFeature = ogr.Feature(featureDefn)
outFeature.SetGeometry(point)
outFeature.SetField(yearField, year)
outFeature.SetField(co2Field, co2)

outLayer.CreateFeature(outFeature)
print "output success!"