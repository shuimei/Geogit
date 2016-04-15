import os
from arcpy import *

os.chdir("E:/ml")
f=open("26843.txt")
fields=['ID','alert','empty','light','highway','brake',
        'recTime','gpsTime','lng','lat','speed','direction','satNum']
def iterCSV(fileOBJ,fields):
    def dictit(line):
        lineTuples=map(lambda x,y:(x,y),fields,line.strip("\n").split(','))
        d={}
        for t in lineTuples:
            d[t[0]]=t[1]
        return d
    return dictit(fileOBJ.next())
