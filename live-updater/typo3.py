#!/home/bin/python
import httplib

#Based on crawling typo3 website and from Typo3 package: introductionpackage-6.0.0

def get_update():
	modules = []
	
	location = '/extensions/repository/'
	print location
	conn = httplib.HTTPConnection('typo3.org')
	conn.request("GET", location)
	r1 = conn.getresponse()
	print r1.status
	pages_number = r1.read().partition('">Last</a>')[0].rpartition("%5D=")[2]
	print int(pages_number)
	
	for i in range(int(pages_number)):
		location = '/extensions/repository/?tx_solr[page]=' + str(i)
		print location
		conn = httplib.HTTPConnection('typo3.org')
		conn.request("GET", location)
		r1 = conn.getresponse()
		#print r1.status
		page = r1.read().split("\n")
		#print page
	
		for elmt in page:
			var = elmt.partition('<span class="ter-ext-list-row-key">')[2].partition("</span")[0]
			if var != '':
				modules.append(var)
	
	return sorted(list(set(modules)))
