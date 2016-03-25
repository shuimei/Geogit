import os


def chunkProc(fileName):
	with open(fileName,'r') as f:
		lines=[x.rstrip('\n') for x in f]
		lines.pop(0)
	return lines

if __name__ == '__main__':
	dataSourceDir=r'F:\codes\python\dianping\entertainment'
	outputDir=r'F:\codes\python\data'
	os.chdir(dataSourceDir)
	fileIter=iter(os.listdir(os.getcwd()))
	with open(outputDir+'\\dianping_entertainment.csv','a+') as output:
		output.write('location,region,category,subcategory,index,addr,name\n')
		for f in fileIter:
			content=chunkProc(f)
			head=f.rstrip('.txt').split("_")
			head.pop(-1)
			for line in content:
				toWrite=','.join(head)+','+line+'\n'
				output.write(toWrite)
			print f
		print 'write over~'



