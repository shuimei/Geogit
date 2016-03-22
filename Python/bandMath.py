import arcpy
import numpy
def bandMath(raster, band1, band2, cal=''):
	raster=arcpy.RasterToNumPyArray(raster)
	calculation = {
		"+": lambda :x+y
		"-": lambda :x-y
		"*": lambda :x*y
		"/": lambda :numpy.float64(x)/y
	}
	if cal is None:
		raise ValueError
		print 'You haven\'t define a method!'
	elif cal not in calculation.keys():
		raise ValueError
		print 'You should define a method with a symbol in ['+','-','*','/']'
	else:
		return calculation[cal](raster[band1],raster[band2])

if __name__ == '__main__':
	inRaster = r''
	outRaster = r''
	band1 = 0
	band2 = 1
	cal = ''
	arcpy.NumPyArrayToRaster(bandMath(inRaster, band1, band2)).save(outRaster)

