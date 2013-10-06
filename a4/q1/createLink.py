#!/usr/bin/python3
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys
COUNT=100
DEFAULT_FILE='../../a3/q1/links.txt'

if len(sys.argv) != 2:
	print('Please pass the path to your link file, defaulting to ' + DEFAULT_FILE)
	path=DEFAULT_FILE
else:
	path=sys.argv[1]

#Get BeautifulSoup HTML parsable object for a link
def parse(link):
	response = urllib.request.urlopen(link)
	soup = BeautifulSoup(response.read())
	response.close()
	return soup

#Return true if the link isnt a bookmark, javascript, mail, etc
def isValid(link):
	return not '#' in link and not 'javascript' in link and not 'mailto' in link

#If relative URI, convert to full
def getFullURI(link,sublink):
	if sublink.startswith('/'):
		netloc=str(urlparse(link).netloc).strip()
		print('Found relative link, adding ' + netloc + ' to ' + sublink)
		link=netloc+sublink
	return link.strip()

#Compute a single link and write to file name
def writeResult(name,link):
	s=set()
	print('Processing site ' + link)
	soup=parse(link)
	for sublinkEle in soup.findAll('a',href=True):
		sublink=str(sublinkEle['href']).strip()
		if isValid(sublink):
			sublink=getFullURI(link,sublink)
			if sublink:
				print('Found link ' + sublink)
				s.add(sublink)
	with open('results/' + name, 'w') as r:
		r.write('site:\n' + link + '\nlinks:\n')
		for sublink in s:
			r.write(sublink + '\n')

with open(path) as f:
	i=0
	for line in f:
		link=line.strip()
		try:
			writeResult(str(i),link)
			i+=1
		except:
			pass
		if i >= COUNT:
			sys.exit()
