#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
The files to be renamed should be in a folder called "sum"
'''

import re, sys, os, random, string, traceback

path = os.path.abspath(os.path.dirname(sys.argv[0])) + "/sum/"

for filename in os.listdir(path):
	
	# this ensures that files that have already been renamed are not re-parsed, assuming that the new filename is less than 100 chars
	if len(filename) > 99:
		with open(path + filename,'r') as l:
			for line in l:
				if "NOTE" in line:
					r = re.search("NOTE: (.*?)_(\d?)_?\('([\d/]*)', '([\d/]*)'\).*",line)
					country = r.group(1)
					part    = r.group(2)
					begin   = r.group(3).replace("/", "_")
					end     = r.group(4).replace("/", "_")
				if "Email Request:" in line:
					docrange = re.search('.*?([\d-]+).*',line).group(1)
					if part == "":
						name = country + ", " + begin + " - " + end + ", " + docrange
					else:
						name = country + ", " + begin + " - " + end + ", " + docrange + " (" + part + ")"
				if "DOCUMENTS" in line:
					name = name + ' of ' + re.search(' +(\d+) of (\d+) DOCUMENTS',line).group(2)
					break
		print name
		os.rename(path + filename, path + name + ".txt")