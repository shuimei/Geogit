import osgeo.ogr as ogr
import osgeo.osr as osr
import sys
import os
import csv

# inFileName=sys.argv[1]
# outputFileName=sys.argv[2]
# inFileName is a plt file path
inFileName=r'some.plt'
layerName=inFileName.rstrip('.plt').split('/')[-1]
outputFileName=layerName+'.shp'
workspace=r'workspace'
os.chdir(workspace)

# set up the shapefile driver
driver = ogr.GetDriverByName("ESRI Shapefile")
data_source = driver.CreateDataSource(outputFileName)

# create the spatial reference, WGS84
srs = osr.SpatialReference()
srs.ImportFromEPSG(4326)
# create the layer
layer = data_source.CreateLayer(layerName, srs, ogr.wkbPoint)

# Add the fields we're interested in\
field_id = ogr.FieldDefn("ID", ogr.OFTString)
field_id.SetWidth(16)
layer.CreateField(field_id)
layer.CreateField(ogr.FieldDefn("Latitude", ogr.OFTReal))
layer.CreateField(ogr.FieldDefn("Longitude", ogr.OFTReal))
layer.CreateField(ogr.FieldDefn("Altitude", ogr.OFTInteger))
layer.CreateField(ogr.FieldDefn("Date", ogr.OFTReal))
layer.CreateField(ogr.FieldDefn("DateString", ogr.OFTString))
layer.CreateField(ogr.FieldDefn("TimeString", ogr.OFTString))

# Process the text file and add the attributes and features to the shapefile
# use a dictionary reader so we can access by field name

with open(inFileName,'rb') as csvFile:
	spamreader = csv.reader(csvFile, delimiter=',')
	for i in xrange(6):
		spamreader.next()
	try:
		while True:
			row = spamreader.next()
			# create the feature
			feature = ogr.Feature(layer.GetLayerDefn())
			# Set the attributes using the values from the delimited text file
			feature.SetField("ID", inFileName.rstrip('.plt'))
			feature.SetField("Latitude", row[0])
			feature.SetField("Longitude", row[1])
			feature.SetField("Altitude", row[3])
			feature.SetField("Date", row[4])
			feature.SetField("DateString", row[5])
			feature.SetField("TimeString", row[6])

			# create the WKT for the feature using Python string formatting
			wkt = "POINT(%f %f)" %  (float(row[1]) , float(row[0]))
			# Create the point from the Well Known Txt
			point = ogr.CreateGeometryFromWkt(wkt)

			# Set the feature geometry using the point
			feature.SetGeometry(point)
			# Create the feature in the layer (shapefile)
			layer.CreateFeature(feature)
			# Destroy the feature to free resources
			feature.Destroy()
	except StopIteration:
		print 'write accomplished!'
data_source.Destroy()
