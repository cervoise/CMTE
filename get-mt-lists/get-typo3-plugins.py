#!/home/bin/python
import httplib
import time

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

date = time.strftime('%y-%m-%d', time.localtime())

result = open('typo3_plugins_list.txt', 'a+')
result.write('#Modules extracted from http://typo3.org/extensions/repository/ on ' + date + "\n")
modules = sorted(list(set(modules)))
for elmt in modules:
    #print elmt
    result.write(elmt + "\n")

result.write('#Other module from introductionpackage-6.0.0')
result.write('introduction\n')

result.close()
