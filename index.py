#!/usr/bin/python

import cgi;
import cgitb;cgitb.enable()

print "Content-Type: text/html"
print ""

import os, sys
from io import BytesIO
from PIL import Image

def compress(rootdir, filename):
	path = os.path.join(rootdir, filename)

	try:
		img    = Image.open(path)
		size   = img.size
		width  = size[0]
		height = size[1]

		if width > 1920:
			ratio  = float(height) / float(width)
			width  = 1920
			height = int(width * ratio)

			img = img.resize((width, height), Image.ANTIALIAS)

		img.save(path, format = "JPEG", quality = 70)
	except IOError:
		pass

"""
	@var string destionation
	Contains a path to the folder with images
"""

destination = '/home/www/domain.com/images/'

for root, subdirs, files in os.walk(destination):
	for filename in files:
		compress(root, filename)