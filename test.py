#!/usr/bin/python2.7 -tt

import sys
import json
import urllib2

def hello(name):
	print "Hello", name

def main():
	url = sys.argv[1]
	data = urllib2.urlopen(url)
	d = json.loads(data.read())
	j = 1
	for i in d:
		print 'Project %d --> %s, %s' % (j, i['name'], i['created_at'])
		j=j+1

if __name__ == '__main__':
	main()


