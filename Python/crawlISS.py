import requests
import os
import random
import time
os.chdir(r'P:\files\data\ISS')
baseURL= "http://eol.jsc.nasa.gov/SearchPhotos/photo.pl?"

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

mission='ISS030'
roll='E'
max=27984
min=5104
randNum=[]
a=0
t=open('count.txt','a+')
while True:
	frame=random.randint(min-1,max+1)
	if frame not in randNum:
		randNum.append(frame)
		crawlISSImages(mission,roll,str(frame))
		t.write(mission+'_'+roll+'_'+str(frame)+'.JPG')
		# print mission+'_'+roll+'_'+str(frame)+'.JPG'
		time.sleep(1)
