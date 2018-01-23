from osgeo import ogr
import math
import os
import time

def deco(func):  
    print func  
    return func 

# Collect all Geometry
@deco
def iterBuffer(inGeom,times=1,error=1):
	area=inGeom.GetArea()
	targetArea=area * times
	presentArea=targetArea+2 * error
	bufferedGeom=inGeom
	smallDis=0
	bigDis=20000.0
	tmpDis=10000.0
	while math.fabs(targetArea-presentArea)>error:
		if targetArea>presentArea:
			smallDis=tmpDis
			tmpDis=(bigDis+smallDis)/2
			bufferedGeom=inGeom.Buffer(tmpDis)
			presentArea=bufferedGeom.GetArea()
		elif targetArea<presentArea:
			bigDis=tmpDis
			tmpDis=(bigDis+smallDis)/2
			bufferedGeom=inGeom.Buffer(tmpDis)
			presentArea=bufferedGeom.GetArea()
		# print tmpDis
		time.sleep(0)
	print tmpDis
	return inGeom.Buffer(tmpDis), times
	# print 'error:',targetArea-presentArea

if __name__ == '__main__':
	# Get a Layer
	year = "2015"
	inShapefile = r"E:\Documents\Lab Issues\chenshengzi\data\%s\%sBI.shp"%(year, year)
	outShapefile = r"E:\Documents\Lab Issues\chenshengzi\data\%s\%sBI_buffer.shp"%(year, year)
	inDriver = ogr.GetDriverByName("ESRI Shapefile")
	inDataSource = inDriver.Open(inShapefile, 0)
	inLayer = inDataSource.GetLayer()
	

	# Create the output shapefile
	outDriver = ogr.GetDriverByName("ESRI Shapefile")
	if os.path.exists(outShapefile):
		outDriver.DeleteDataSource(outShapefile)
	outDataSource = outDriver.CreateDataSource(outShapefile)
	outLayer = outDataSource.CreateLayer("buffers", geom_type=ogr.wkbPolygon)
	# Add an ID field
	idField = ogr.FieldDefn("originID", ogr.OFTInteger)
	outLayer.CreateField(idField)
	bufferTimes = ogr.FieldDefn("times",ogr.OFTInteger)
	outLayer.CreateField(bufferTimes)
	# Get the output Layer's Feature Definition
	featureDefn = outLayer.GetLayerDefn()

	layerDefinition = inLayer.GetLayerDefn()
	for i in range(layerDefinition.GetFieldCount()):
	    print layerDefinition.GetFieldDefn(i).GetName()
	for feature in inLayer:
		fid = feature.GetField(0)
		inGeom = feature.GetGeometryRef()
		# iterBuffers=[iterBuffer(inGeom,times=i,error=1) for i in xrange(1,16)]
		iterBuffers=[iterBuffer(inGeom,times=i,error=1) for i in xrange(2,3)]
		# buffer1=iterBuffer(inGeom,times=15,error=0.001)
		for bufferGeom in iterBuffers:
			# create a new feature
			outFeature = ogr.Feature(featureDefn)
			outFeature.SetGeometry(bufferGeom[0])
			outFeature.SetField("originID",fid)
			outFeature.SetField("times",bufferGeom[1])
			outLayer.CreateFeature(outFeature)
		# print "buffer succed"
	# Close DataSource
	inDataSource.Destroy()
	outDataSource.Destroy()






# # Save a new Shapefile
# outShapefile = "self_defined.shp"
# outDriver = ogr.GetDriverByName("ESRI Shapefile")
# if os.path.exists(outShapefile):
#     outDriver.DeleteDataSource(outShapefile)
# # Create the output shapefile
# outDataSource = outDriver.CreateDataSource(outShapefile)
# outLayer = outDataSource.CreateLayer("self_defined.shp", geom_type=ogr.wkbPolygon)