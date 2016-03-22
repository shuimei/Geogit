import arcpy
from arcpy import env 
import os
workspace=r'filepath'

env.workspace=workspace
os.chdir(env.workspace)
inputTables = [fileName for fileName in  os.listdir(env.workspace) if fileName[-3:]=='dbf']

for input in inputTables:
	arcpy.TableToExcel_conversion(input, input.rstrip('dbf')+'xls')
	print 'input conversed~'

