#!/home/bin/python
import httplib
import os

#from https://raw.githubusercontent.com/wpscanteam/vulndb/master/plugins_full.txt

def get_update():
	domain = "raw.githubusercontent.com"
	conn = httplib.HTTPSConnection(domain)
	location = "/wpscanteam/vulndb/master/plugins_full.txt"
	conn.request("GET", location)
	r1 = conn.getresponse()
	
	temp_file = open('wordpress_plugins_temp.txt', 'a+')
	temp_file.write(r1.read())
	temp_file.close()
		
	plugins_list = []
	
	temp_file = open('wordpress_plugins_temp.txt', 'r+')
	for elmt in temp_file.readlines():
		plugins_list.append(elmt.rstrip())
	temp_file.close()
	os.remove('wordpress_plugins_temp.txt')

	return plugins_list
