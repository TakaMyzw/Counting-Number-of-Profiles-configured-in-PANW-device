# Counting # of configured security profiles
# tested with exported configuration xml file from PAN-OS 5.0
# 
# usage : count_num_of_profiles.py filename
#

import xml.etree.ElementTree as ET
import sys

n = 7
prof_count=n*[0]

#tree = ET.parse('../../Downloads/0709_2')
tree = ET.parse(sys.argv[1])
root = tree.getroot()
profile = root.findall(".//profiles")

# shared object
for element in root.findall("./shared"):
	if element.find('profiles') is not None:
		cnt = len(element.findall('profiles/virus/entry'))
		prof_count[0] += cnt
		cnt = len(element.findall('profiles/spyware/entry'))
		prof_count[1] += cnt
		cnt = len(element.findall('profiles/vulnerability/entry'))
		prof_count[2] += cnt
		cnt = len(element.findall('profiles/url-filtering/entry'))
		prof_count[3] += cnt
		cnt = len(element.findall('profiles/file-blocking/entry'))
		prof_count[4] += cnt
		cnt = len(element.findall('profiles/dos-protection/entry'))
		prof_count[5] += cnt
		cnt = len(element.findall('profiles/data-filtering/entry'))

# vsys object
for element in root.findall(".//vsys/entry"):
	if element.find('profiles') is not None:
#		print element.attrib
		cnt = len(element.findall('profiles/virus/entry'))
		prof_count[0] += cnt
		cnt = len(element.findall('profiles/spyware/entry'))
		prof_count[1] += cnt
		cnt = len(element.findall('profiles/vulnerability/entry'))
		prof_count[2] += cnt
		cnt = len(element.findall('profiles/url-filtering/entry'))
		prof_count[3] += cnt
		cnt = len(element.findall('profiles/file-blocking/entry'))
		prof_count[4] += cnt
		cnt = len(element.findall('profiles/dos-protection/entry'))
		prof_count[5] += cnt
		cnt = len(element.findall('profiles/data-filtering/entry'))
		prof_count[6] += cnt

print prof_count
print sum(prof_count)
