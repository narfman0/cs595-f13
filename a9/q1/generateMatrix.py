#!/usr/bin/python3
import feedparser,re,sys

COUNT=500

#return clean list of matrix worthy words. Someone timed fastest way here:
#http://stackoverflow.com/questions/1276764/stripping-
#everything-but-alphanumeric-chars-from-a-string-in-python
pattern = re.compile('[\W_]+')
def clean(words):
    return pattern.sub('', words).lower()

def getCounts(url,totals):
    s=set()
    feed=feedparser.parse(url)
    for entry in feed.entries:
        words = ''
        if 'title' in entry:
            words += ' ' + entry.title
        elif 'summary' in entry:
            words += ' ' + entry.summary
        else:
            print('No title or summary for URL: ' + url)
        s.update([clean(word) for word in words.split(' ') if word!=''])
    for word in s:
        totals[word]=1+totals.get(word,0)
    return s

totals={}
urlCounts={}
with open('atoms.txt') as f:
    for url in f.readlines():
        s=getCounts(url, totals)
        urlCounts[url]=s
totalTuples=sorted(totals.items(), key=lambda x: x[1])
with open('blogdata.txt','w') as f:
    for word in totalTuples[0:COUNT]:
        f.write(word[0] + ' ')
    for url in urlCounts.keys():
        f.write(url)
        for word in totalTuples[0:COUNT]:
            if word in urlCounts[url]:
                f.write(' ' + str(urlCounts[url][word]))
            else:
                f.write(' 0')
        f.write('\n')
