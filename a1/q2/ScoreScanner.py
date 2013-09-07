#!/usr/bin/python3
#url manipulation: http://docs.python.org/3.1/howto/urllib2.html
#arguments: http://www.diveintopython.net/scripts_and_streams/command_line_arguments.html
#initial bs: http://www.crummy.com/software/BeautifulSoup/
#some bs: http://www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup/
#rest from eclipse ide syntax help
import sys
import time
import urllib.request
from bs4 import BeautifulSoup

if len(sys.argv) != 4:
    print('Usage: ./ScoreScanner.py teamName waitTime uri')
    print('  Where teamName is your favorite team, e.g. South Carolina')
    print('    waitTime is a timeout between refreshing the scores, e.g. 5')
    print('    uri is the scores.espn.go.com child representing the database from which to draw, e.g. http://scores.espn.go.com/ncf/scoreboard?confId=80&seasonYear=2013&seasonType=2&weekNumber=1')
    print('Since you left these arguments blank, assuming defaults')
    sys.argv=['script','South Carolina','5','http://scores.espn.go.com/ncf/scoreboard?confId=80&seasonYear=2013&seasonType=2&weekNumber=1']

school=sys.argv[1]
sleepTime=int(sys.argv[2])
uriScores=sys.argv[3]

while 1:
    #get html
    response = urllib.request.urlopen(uriScores)
    soup = BeautifulSoup(response.read())
    response.close()

    #iterate over each university matching. don't know if there are any similar schools but why not.
    for university in soup.findAll('a',{'title':school}):
        game = university.findParent().findParent().findParent().findParent().findParent()
        home = game.find('div', {"class":"team home"})
        homeName = home.find('p', {"class":"team-name"}).find('a').string
        homePoints = home.find('li', {"class":"final"}).string
        visitor = game.find('div', {"class":"team visitor"})
        visitorName = visitor.find('p', {"class":"team-name"}).find('a').string
        visitorPoints = visitor.find('li', {"class":"final"}).string
        print(homeName + ': ' + homePoints + ' - ' + visitorName + ': ' + visitorPoints)
    time.sleep(sleepTime)
