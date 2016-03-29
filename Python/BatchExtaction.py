# Import system modules
import os
import arcpy
from arcpy import env
from arcpy.sa import *
# Necessary data folders
originFolder = r'B:\files\data\night_light_data\allraster\origin_stable'
radianceFolder = r'B:\files\data\night_light_data\Radiance Calibration\tar'
saturatedFolder = r'B:\files\data\night_light_data\allraster\calibrated'
maskFolder = r'B:\files\data\MGISDATA\mgisdata\World\other_countries'
workFolder = r'C:\Users\GIS336\Desktop\files\tmp'

# specify files to be applied in Extractions
def SpecifyFiles(folder, postfix):
	return filter(lambda name:name[-len(postfix):] == postfix, os.listdir(folder))

# Execute ExtractByMask and Save the output
def ExtractByMask(inRaster,inMaskData,outputPath, outputPostfix):
	arcpy.CheckOutExtension("Spatial")
	outExtractByMask = ExtractByMask(inRaster,inMaskData)
	outExtractByMask.save(outputPath)

def BatchExtraction(rasterFolder,rasterPostfix,maskFolder,maskPostfix,workFolder):
	rasters = SpecifyFiles(rasterFolder,rasterPostfix)
	masks = SpecifyFiles(maskFolder,maskPostfix)
	for raster in rasters:
		outputDir = workFolder+'\\'+raster.split(".")[0]
		os.mkdir(outputDir)
		for mask in masks:
			outputPath = outputDir + "\\" + mask[:-(len(maskPostfix)+1)] + "." + rasterPostfix
			ExtractByMask(rasterFolder+"\\"+raster, maskFolder+"\\"+mask, outputPath, rasterPostfix)
if __name__ == "__main__":
	BatchExtraction(originFolder,"tif",maskFolder,"shp",workFolder)


