#!/usr/bin/python3
import feedparser,re,sys

COUNT=500

#return clean list of matrix worthy words. Someone timed fastest way here:
#http://stackoverflow.com/questions/1276764/stripping-
#everything-but-alphanumeric-chars-from-a-string-in-python
#Stop words from http://www.ranks.nl/resources/stopwords.html
pattern = re.compile('[\W_]+')
stopWords=[]
with open('stopWords.txt') as f:
    for line in f.readlines():
        stopWords.append(pattern.sub('', line))
def clean(words):
    return pattern.sub('', words).lower()

def getCounts(url,totals):
    s={}
    feed=feedparser.parse(url)
    for entry in feed.entries:
        words = ''
        if 'title' in entry:
            words += ' ' + entry.title
        elif 'summary' in entry:
            words += ' ' + entry.summary
        else:
            print('No title or summary for URL: ' + url)
        for word in words.split(' '):
            cleanedWord=clean(word)
            if cleanedWord != '':
                s[cleanedWord]=1+s.get(cleanedWord,0)
    for word in s.keys():
        totals[word]=s[word]+totals.get(word, 0)
    return s

def getSortedWordCounts():
    urlCounts={}
    totals={}
    i=0
    with open('atoms.txt') as f:
        for line in f.readlines():
            url=line.strip()
            urlCounts[url]=getCounts(url, totals)
            i+=1
            print('Finished URL ' + str(i) + ' ' + url)
    for stopWord in stopWords:
        if stopWord in totals:
            del totals[stopWord]
    return urlCounts,sorted(totals.items(), key=lambda x: 
        x[1],reverse=True)[0:COUNT]

def writeBlogcounts(totalTuples,urlCounts):
    with open('blogdata.txt','w') as f:
        f.write('Table')
        for word in totalTuples:
            f.write(' ' + word[0])
        f.write('\n')
        for url in urlCounts.keys():
            f.write(url)
            for word in totalTuples:
                if word[0] in urlCounts[url]:
                    f.write(' ' + str(urlCounts[url][word[0]]))
                else:
                    f.write(' 0')
            f.write('\n')

urlCounts,totals=getSortedWordCounts()
print('Top results: ' + str(totals))
writeBlogcounts(totals,urlCounts)
