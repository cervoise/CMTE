#!/home/bin/python

# CMTE- CMS Modules and Themes Enemerator
# Copyright (C) 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import sys
import fileinput
import httplib

__CMD__ = {
        "help": "CMS Modules & Themes Enumerator\n"
                "Version 0.2 Antoine Cervoise\n"
                ">>> cmte.py url\n"
                ">>> cmte.py url port"
}

__DEBUG_MODE___ = False

def use_https():
        print "\nUse HTTPS:"
        https = -1
    	while (https < 0 or https > 1):
        	try:
           		https = int(raw_input('---> '))
        	except ValueError:
           		print("That's not an int!")
        return https

def choose_cms():
        cms_list = []
    	i = 0
           		
    	print "\nChoose your CMS:"
    
    	for elmt in fileinput.input(['cms-list.txt']):
        	if elmt[0] != "#":
            		cms_list.append(elmt.rstrip().split(":"))
            		print "[" + str(i+1) + "]: " + cms_list[i][0]
           	 	i += 1
            
    	cms = 0
    	while (cms < 1 or cms > i):
        	try:
           		cms = int(raw_input('---> '))
        	except ValueError:
           		print("That's not an int!")
                  		
        return cms_list[cms-1]

def check_modules(url, port, https, modules_path, modules_list):
	
        modules_found = []
        path =  url.partition("/")[2]
        
        if __DEBUG_MODE___:
                print url
                print modules_list
        
        print "\nAfter scan, try to go " + url + "/" + modules_path + ", you could get more info.\n"

        if __DEBUG_MODE___ is False:
                i = 0
                print str(len(modules_list)) + " modules or themes to check"

        for elmt in modules_list:
                if __DEBUG_MODE___ is False:
                        i += 1
                        sys.stdout.write("\r%d modules or themes already checked" %i)
                        sys.stdout.flush()
		if elmt[0] != '#':
                        if https:
        	                conn = httplib.HTTPSConnection(url.partition("/")[0], port)
                        else :
        	                conn = httplib.HTTPConnection(url.partition("/")[0], port)
        	        location = "/"
        	        if url.partition("/")[2] != '':
        	        	location += url.partition("/")[2] + "/"
        	        location += modules_path + "/" + elmt + "/"
        	        conn.request("GET", location)
        	        r1 = conn.getresponse()
                    
        	        if __DEBUG_MODE___:
        	        	print location
        	            	print elmt
		                print r1.status
                    	
        	        if r1.status == 200 or r1.status == 403:
        	                modules_found.append(elmt.split("/")[0])
                        	
        return sorted(list(set(modules_found)))

def main():	
        if len(sys.argv) == 1:
                print __CMD__["help"]
        else:
                url = sys.argv[1]
                port= 80
                if len(sys.argv) > 2:
                        port = sys.argv[2]
                
                https = use_https()
                cms = choose_cms()
                if __DEBUG_MODE___:
                        for elmt in cms:
                                print elmt
    
                modules_list = []
                for elmt in fileinput.input(['databases/'+ cms[0] + '.txt']):
                        modules_list.append(elmt.rstrip())
    
                modules_found = check_modules(url, port, https, cms[1], modules_list)

                if len(modules_found) > 0:
                        print "\n" + str(len(modules_found)) + " module(s) or theme(s) found:"   
                        for module in modules_found:
                                print module
                else:
                        print "\nNo module or theme found."
                        
if __name__=="__main__":
	main()
