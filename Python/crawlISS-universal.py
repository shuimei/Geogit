import requests
import os
import random
import time
import sys


def genURL(mission,roll,frame):
	return baseURL+'?mission='+mission+'&roll='+roll+'&frame='+frame
def crawlISSImages(mission,roll,frame):
	url='http://eol.jsc.nasa.gov/DatabaseImages/ESC/large/'+mission+'/'+mission+'-'+roll+'-'+frame+'.JPG'
	r=requests.get(url)
	c=r.content
	if len(c)>100000:
		with open(mission+'_'+roll+'_'+frame+'.JPG','wb') as f:
			f.write(c)
			print mission+'_'+roll+'_'+frame+'.JPG'

if __name__=="__main__":
	
	baseURL= "http://eol.jsc.nasa.gov/SearchPhotos/photo.pl?"
	mission=raw_input('input mission name:\n')
	roll='E'
	max=raw_input("input max frame:\n")
	min=raw_input("input min frame:\n")
	os.chdir(str(raw_input("input image folder:\n")))
	randNum=[]
	t=open('count.txt','a+')
	while True:
		frame=random.randint(int(min)-1,int(max)+1)
		if frame not in randNum:
			randNum.append(frame)
			crawlISSImages(mission,roll,str(frame))
			t.write(mission+'_'+roll+'_'+str(frame)+'.JPG\n')
			# print mission+'_'+roll+'_'+str(frame)+'.JPG'
			time.sleep(0.1)
	t.close()