#!/home/bin/python

import typo3
import wordpressThemes
import wordpressPlugins

def get_old_db(cms):
	database_file = open("../databases/" + cms + ".txt", "r")
	module_list = []
	for elmt in database_file.readlines():
		if elmt[0] != "#":
			module_list.append(elmt.rstrip())
	database_file.close()
	return module_list

def get_new_db(cms):
	if cms == 'typo3':
		return typo3.get_update()
	elif cms == 'wordpress_themes':
		return wordpressThemes.get_update()
	elif cms == 'wordpress_plugins':
		return wordpressPlugins.get_update()
	elif cms == 'spip3_plugins':
		return spip3Plugins.get_update()
	elif cms == 'spip1and2_plugins':
		return spip1and2Plugins.get_update()

def livee_update(cms):
	new_list = get_new_db(cms)
	old_list = get_old_db(cms)
	all_list = list(set(new_list + old_list))
	database_file = open('../databases/' + cms + ".txt", "w")
	for elmt in all_list:
		database_file.write(elmt + "\n")
	database_file.close()
	
def update_all():
	updatable_cms = []
	updatable_cms.append("typo3")
	updatable_cms.append("wordpress_themes")
	updatable_cms.append("wordpress_plugins")
	updatable_cms.append("spip1and2_plugins")
	updatable_cms.append("spip3_plugins")
	for cms in updatable_cms:
		live_update(cms)
	
update_all()
