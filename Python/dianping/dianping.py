import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
headers = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, sdch",
"Accept-Language":"zh-CN,zh;q=0.8",
"Connection":"keep-alive",
"Cookie":'PHOENIX_ID=0a01677b-153a2910bd6-153f1e3; _hc.v="\"ef538059-0bf9-4edd-a247-2a2cc2af0d83.1458721328\""; s_ViewType=10; thirdtoken=1278042DB5B105F41D96E7A7E3FB92EF; JSESSIONID=1278042DB5B105F41D96E7A7E3FB92EF; aburl=1; cy=1; cye=shanghai; dper=d6f5abbb3a914c8bc165423a0b86488eb3afe0bc46389f70362e6ea98be46197; ll=7fd06e815b796be3df069dec7836c3df; ua=betasydiandian; ctu=0561fd0097f403570561ae5b62477e7cef56e7051a9f5653d49e80e50485fa2b; uamo=18018562022',
"DNT":1,
"Host":"www.dianping.com",
"Upgrade-Insecure-Requests":1,
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36"
}

def makeURL(root, location='1', region='r1', page='p1', category='20',subcategory='g114'):
	"""
	generatte url to be crawled
	root: root url,
	location: city name,
	region: local district,
	page: page number
	category:,
	subcategory:,
	"""
	return root+location+'/'+category+'/'+subcategory+region+page

def makeRequests(url,headers):
	response=requests.get(url,headers=headers)
	content=response.content
	return content

def getInfoTable(content):
	soup=bs(content,'html5lib')
	divs = soup.find_all('div',id='shop-all-list')
	name=[]
	addr=[]
	comment=[]
	price=[]
	score=[]
	b=[]
	
	udiv=unicode(divs[0])
	lists = bs(udiv, 'html5lib')
	for i in lists.find_all('h4'):
		name.append(i.text)
	for i in lists.find_all('span','addr'):
		addr.append(i.text)
	for i in lists.find_all('b'):
		b.append(i.text)
		
	for bb in b:
		if '.' in bb:
			score.append(bb)


	table = pd.DataFrame(
	        {
	        'name':name,
	        'addr':addr,
	        }
	    )
	return table

if __name__ == '__main__':
	root='http://www.dianping.com/search/category/'
	parameters={
		'location':'1',
		'regions':['r1','r2','r3','r4','r5','r6','r7','r8','r9','r10','r12','r13','r5937','r5939','r8846','r8847','r5938','c3580'],
		'category':{
			'food':'10',
			'shopping':'20',
			'entertainment':'30'},
		'food':['g114', 'g101','g113', 'g132', 'g112', 'g117', 'g110', 'g116', 'g111', 'g103', 'g508', 'g102', 'g115', 'g109', 'g106', 'g104', 'g248', 'g3243', 'g251', 'g26481', 'g203', 'g107', 'g105', 'g108', 'g118', 'g133', 'g134', 'g246', 'g247', 'g249', 'g250', 'g252', 'g311', 'g26482', 'g26484'],
		'entertainment':['g135','g141','g14','g132','g1','g20041','g5672','g20042','g144','g2004','g2754','g20038','g6694','g32732','g137','g134','g156','g20039','g2827','g142','g136','g2649'],
		'shopping':['g120','g187','g119','g235','g125','g27809','g27810','g27811','g27812','g128','g123','g122','g6715','g6716','g6717','g26085','g124','g121','g127','g126','g6828','g6827','g6829','g6830','g20020','g20022','g20023','g20025','g32703','g32705','g129'],
		'conference':['g165','g3014','g3016','g3018','g1040','g1191','g2738','g2740',],
		'beauty':['g157','g158','g33761','g148','g149','g2898','g159','g493','g123','g2572','g183','g2790','g6700'],
		'life service':['g26465','g237','g181','g4607','g26117','g195','g835','g612','g197','g980','g836','g2929','g32742','g2932',]
		}
	# region set url parameters
	location=parameters['location']
	regions=parameters['regions']
	category=parameters['category']['shopping']
	subcategories=parameters['shopping']
	workSpaceDir='./dianping'
	folder='shopping/'
	# should be set

	failURL=[]
	for region in regions:
		for subcategory in subcategories:
			pages=map(lambda x:'p'+str(x),range(1,51))
			for page in pages:
				try:
					requestURL=makeURL(root,page=page,region=region,category=category, subcategory=subcategory)
					print requestURL
					table=getInfoTable(makeRequests(requestURL,headers))
					fileName='./dianping/'+folder+location+'_'+region+'_'+category+'_'+subcategory+'_'+page+'.txt'
					table.to_csv(fileName,encoding='utf-8')
					time.sleep(1)
				except IndexError:
					print 'page end'
					break
				except requests.exceptions.ConnectionError:
					print 'failed:'+requestURL
					failURL.append(requestURL)
					pass
	print 'the world comes back to peace!\n'
	for f in failURL:
		print f


