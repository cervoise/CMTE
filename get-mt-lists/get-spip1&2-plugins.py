#!/home/bin/python
import httplib
import time

def get_pages_number(version):
    location = '/spip.php?page=plugins&compatible_spip=' + version
    print location
    conn = httplib.HTTPConnection('plugins.spip.net')
    conn.request("GET", location)
    r1 = conn.getresponse()
    print r1.status
    pages_number = r1.read().partition('class="next"')[0].rpartition("'nofollow'>")[2].partition('</a>')[0]
    return int(pages_number)

def add_modules(modules_list, version):
    for i in range(get_pages_number(version)):
        location = '/spip.php?page=plugins&compatible_spip=3.0&debut_plugins=' + str(i*20)
        print location
        conn = httplib.HTTPConnection('plugins.spip.net')
        conn.request("GET", location)
        r1 = conn.getresponse()
        #print r1.status
        page = r1.read().split("\n")
        #print page

        for elmt in page:
            var = elmt.partition('<strong><a href="')[2].partition('.html')[0]
            if var != '':
                    modules.append(var)
modules = []

add_modules(modules, '1.9')
add_modules(modules, '2.0')
add_modules(modules, '2.1')

date = time.strftime('%y-%m-%d', time.localtime())

result = open('spip1&2_plugins_list.txt', 'a+')
result.write('#Modules extracted from http://plugins.spip.net on ' + date + "\n")
modules = sorted(list(set(modules)))
for elmt in modules:
    #print elmt
    result.write(elmt + "\n")

result.close()
