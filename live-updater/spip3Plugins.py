#!/home/bin/python
import httplib

#Modules extracted from http://plugins.spip.net

def get_pages_number(version):
    location = '/spip.php?page=plugins&compatible_spip=' + version
    print location
    conn = httplib.HTTPConnection('plugins.spip.net')
    conn.request("GET", location)
    r1 = conn.getresponse()
    print r1.status
    pages_number = r1.read().partition('class="pages"')[2].rpartition("'nofollow'>")[2].partition('</a>')[0]
    print pages_number
    return int(pages_number)/20 + 1

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
                    modules_list.append(var)


def get_update():
	modules = []
	
	add_modules(modules, '3.0')
	add_modules(modules, '3.1')
	
	return sorted(list(set(modules)))
