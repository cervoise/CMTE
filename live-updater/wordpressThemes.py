#!/home/bin/python
import httplib
import os

#from https://github.com/wpscanteam/vulndb/master/master/plugins_full.txt

def get_update():
	domain = "raw.githubusercontent.com"
	conn = httplib.HTTPSConnection(domain)
	location = "/wpscanteam/vulndb/master/themes_full.txt"
	conn.request("GET", location)
	r1 = conn.getresponse()
	
	temp_file = open('wordpress_themes_temp.txt', 'a+')
	temp_file.write(r1.read())
	temp_file.close()
		
	themes_list = []
	
	temp_file = open('wordpress_themes_temp.txt', 'r+')
	for elmt in temp_file.readlines():
		themes_list.append(elmt.rstrip())
	temp_file.close()
	os.remove('wordpress_themes_temp.txt')
		
	return themes_list
