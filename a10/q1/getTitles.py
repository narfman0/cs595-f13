#!/usr/bin/python3
import sys
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse
import feedparser
import traceback

DEFAULT_COUNT=100
DEFAULT_SOURCES='http://musicliberation.blogspot.com/search?max-results=100','http://musicliberation.blogspot.com/search?updated-max=2013-02-26T21:19:00Z&max-results=100&start=25&by-date=false','http://musicliberation.blogspot.com/search?updated-max=2013-02-26T21:19:00Z&max-results=100&start=25&by-date=false','http://musicliberation.blogspot.com/search?updated-max=2012-02-14T13:33:00Z&max-results=100&start=79&by-date=false','http://musicliberation.blogspot.com/search?updated-max=2011-12-27T12:48:00Z&max-results=100&start=93&by-date=false','http://musicliberation.blogspot.com/search?updated-max=2011-10-20T13:05:00%2B01:00&max-results=100&start=116&by-date=false'
if len(sys.argv) != 3:
    print('Pass the count, defaulting to ' + str(DEFAULT_COUNT))
    print('Pass the blog, defaulting to ' + str(DEFAULT_SOURCES))
    count=DEFAULT_COUNT
    urls=DEFAULT_SOURCES
else:
    count=sys.argv[1]
    urls=sys.argv[2]

def parse(link):
    response = urllib.request.urlopen(link)
    soup = BeautifulSoup(response.read())
    response.close()
    return soup

def getEntries(max,urls):
  entries=[]
  for url in urls:
    soup=parse(url)
    for entry in soup.findAll('h3'):
      try:
        title=str(list(list(entry.children)[1].children)[0])
        if 'Reviewed by' not in title and title.strip() != '' and title not in entries:
          entries.append(title)
          if max <= len(entries):
            return entries
      except:
        print('Error on entry: ' + str(entry))
  return entries

entries=getEntries(100,urls)
print('Found ' + str(len(entries)) + ' entries. Contents:\n' + str(entries))
with open('titles.txt','w') as f:
  for entry in entries:
    f.write(entry + '\n')
