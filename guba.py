#!/usr/bin/python

import urllib2
import re
import codecs
import sys

def getHtml(url):
	page=urllib2.urlopen(url)
	type = sys.getfilesystemencoding() 

	html = page.read()
	html = html.decode("utf-8").encode(type)
	print html
	return html





if __name__=="__main__":
	url='http://guba.eastmoney.com/remenba.aspx?type=1'
	getHtml(url)
