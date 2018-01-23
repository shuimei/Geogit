__author__ = 'Z0ki'
import arcpy
import numpy
import xlwt
import os
import math
from arcpy import env
import pickle


def getList(workspace, startWith):
    returnList = []
    fileList = os.listdir(workspace)
    for file in fileList:
        if str.startswith(file, startWith) and str.endswith(file, ".shp"):
            returnList.append(file[0:-4])
    return returnList


def writeExcel(path, excelName, SheetName, headList, numpyArray):
    fileName = path + "\\" + excelName
    book = xlwt.Workbook()
    sheet1 = book.add_sheet(SheetName)
    headRow = sheet1.row(0)
    for i in range(0, len(headList)):
        headRow.write(i, headList[i])

    for i in range(0, numpy.shape(numpyArray)[0]):
        for j in range(0, len(headList)):
            sheet1.write(i + 1, j, numpyArray[i][j])

    book.save(fileName)
    print('Done!')


def GetMinimumValue(head_tail_ratio_diff_List):
    minimum_diff = min(head_tail_ratio_diff_List)
    minimum_diff_index = head_tail_ratio_diff_List.index(minimum_diff)
    if minimum_diff_index == 0:
        if len(head_tail_ratio_diff_List) > 1:
            head_tail_ratio_diff_List.remove(minimum_diff)
            minimum_diff = min(head_tail_ratio_diff_List)
            # minimum_diff_index = head_tail_ratio_diff_List.index(minimum_diff)
    return minimum_diff


def extractNaturalCity(dmspRaster, vectorName):
    meanDMSPObject = arcpy.GetRasterProperties_management(dmspRaster, "MEAN")
    meanDMSP = float(meanDMSPObject.getOutput(0))
    countRaster = arcpy.sa.Con(dmspRaster < meanDMSP, 0, 1)
    naturalRaster = arcpy.sa.SetNull(dmspRaster < meanDMSP, dmspRaster)
    rows = arcpy.SearchCursor(countRaster)
    # outputString = ""
    count0 = 0
    count1 = 0
    for row in rows:
        if str(row.value) == "0":
            count0 = int(str(row.count))
        elif str(row.value) == "1":
            count1 = int(str(row.count))
        else:
            print "Strange Value!"

    countTotal = count0 + count1
    ratio0 = float(count0) / float(countTotal)
    ratio1 = float(count1) / float(countTotal)
    head_tail_ratio_diff = math.fabs(ratio1 - ratio0)
    resultList = []
    resultList.append(vectorName)
    resultList.append(countTotal)
    resultList.append(meanDMSP)
    resultList.append(count1)
    resultList.append(ratio1)
    resultList.append(count0)
    resultList.append(ratio0)
    resultList.append(head_tail_ratio_diff)
    return [resultList, naturalRaster, head_tail_ratio_diff]


def main(inRasterDir, outObj):
    arcpy.CheckOutExtension("Spatial")
    inRasters = filter(lambda r: r[-3:] == "tif", os.listdir(inRasterDir))
    env.workspace = inRasterDir
    dmspRasters = map(arcpy.Raster, inRasters)
    for d_r in dmspRasters:
        v_n = d_r.name.split(".")[0]
        totalList = []
        finalTotalList = []

        totalList_single_vector = []
        head_tail_ratio_diff_List = []

        ratio_head = 0
        round = 0
        while (round < 2 or ratio_head < 0.5):
            print round
            tempList = extractNaturalCity(d_r, v_n)
            temList2 = tempList[0]
            d_r = tempList[1]
            head_tail_ratio_diff_List.append(tempList[2])
            tempList = []
            totalList.append(temList2)
            totalList_single_vector.append(temList2)
            ratio_head = float(temList2[4])
            round = round + 1

        minimum_diff = GetMinimumValue(head_tail_ratio_diff_List[:])
        minimum_diff_index = head_tail_ratio_diff_List.index(minimum_diff) - 1
        if minimum_diff_index < 0:
            minimum_diff_index = 0
        finalTotalList.append(totalList_single_vector[minimum_diff_index])
        threshold = totalList_single_vector[minimum_diff_index]
        output = open(r"%s\%s_dot5.pkl" % (outObj, v_n), "wb")
        pickle.dump(threshold, output)
        print threshold
        print "%s done." % v_n
        print "next one"


if __name__ == "__main__":
    main(r"G:\Nighttime Light Data\Continents\Africa", r"G:\Stock Estimation Study\Threshold")

