#!/home/bin/python
import httplib
import time

modules = []

location = '/project/project_module?page=0&f[0]=&f[1]=&f[2]=&f[3]=&f[4]=sm_field_project_type%3A[*%20TO%20*]&text=&solrsort=iss_project_release_usage%20desc&op=Search'
#print location
conn = httplib.HTTPSConnection('drupal.org')
conn.request("GET", location)
r1 = conn.getresponse()
pages_number = r1.read().partition('<a title="Go to last page"')[2].partition('"last')[0]
pages_number = pages_number.partition('page=')[2].partition('&amp')[0]
#print int(pages_number)

for i in range(int(pages_number)):
    location = '/project/project_module?page=' + str(i) + "&f[0]=&f[1]=&f[2]=&f[3]=&f[4]=sm_field_project_type%3A[*%20TO%20*]&text=&solrsort=iss_project_release_usage%20desc&op=Search"
    conn = httplib.HTTPSConnection('drupal.org')
    conn.request("GET", location)
    r1 = conn.getresponse()
    #print r1.status
    page = r1.read().split("\n")
    #print page

    for elmt in page:
        var = elmt.partition('<h2><a href="/project/')[2].partition('">')[0]
        if var != '':
          modules.append(var)
          print var

date = time.strftime('%y-%m-%d', time.localtime())

result = open('drupal_modules_list.txt', 'a+')
result.write('#Modules extracted from http://drupal.org on ' + date + "\n")
modules = sorted(list(set(modules)))
for elmt in modules:
    #print elmt
    result.write(elmt + "\n")

result.close()

