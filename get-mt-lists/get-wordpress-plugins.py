#https://raw.github.com/wpscanteam/wpscan/master/data/plugins_full.txt

import httplib
import time

date = time.strftime('%y-%m-%d', time.localtime())

url = "raw.github.com"
conn = httplib.HTTPSConnection(url)
location = "/wpscanteam/wpscan/master/data/plugins_full.txt"
conn.request("GET", location)
r1 = conn.getresponse()

result = open('wordpress_plugins_list.txt', 'a+')
result.write('#Modules extracted from https://github.com/wpscanteam/wpscan/master/data/plugins_full.txt on ' + date + "\n")
result.write(r1.read())
result.close()
