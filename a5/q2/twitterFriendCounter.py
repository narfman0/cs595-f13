#!/bin/python3
from __future__ import unicode_literals
import numpy
from numpy import array
import requests
from requests_oauthlib import OAuth1
import urllib
from urllib.parse import urlparse
import sys
import time

CONSUMER_KEY = "dbr6Ce0ahKsr4QMyIxElQ"
CONSUMER_SECRET = "Bxd17G6TSr74lDzpGkl9ThQRqE5HwDtrPofdJninKLA"
OAUTH_TOKEN = "589075411-qVWno21brc3Kjw24Wg6UeDJVHBE6DsrRbd7r0gGU"
OAUTH_TOKEN_SECRET = "fLEC8DJvPqginylDhhCm0F9xNS2R6Xc8djk6DbVlVI"
LIST_URI = 'https://api.twitter.com/1.1/followers/list.json'
TARGET='phonedude_mln'
ERROR_TIME=10
RATE_TIME=15*60
RATE_EXCEEDED_MESSAGE='Rate limit exceeded'

def parse_arguments():
    if len(sys.argv) != 2:
        print('Please pass the screen_name of the user from which ' +
            ' you wish to measure, defaulting to ' + TARGET)
        return TARGET
    else:
        return sys.argv[1]

def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

def get_followers(oauth, screen_name):
    s=[]
    cursor = -1
    while cursor != 0:
        while True:
            r = requests.get(url=LIST_URI + '?screen_name=' + screen_name +
                '&count=200&cursor=' + str(cursor), auth=oauth)
            json=r.json()
            if 'errors' in json:
                if RATE_EXCEEDED_MESSAGE in json['errors'][0]['message']:
                    print('Sleeping from rate error')
                    time.sleep(RATE_TIME)
                else:
                    print('Sleeping from non-rate error')
                    time.sleep(10)
            else:
                break;
        if 'next_cursor' in json:
            cursor = json['next_cursor']
        else:
            cursor = 0
        if 'users' in json:
            for user in json['users']:
                s.append(user['screen_name'])
    return s

def twitter_search(oauth, target):
    followers=get_followers(oauth, target)
    requests=1
    print('Found ' + str(len(followers)) + ' followers, names: ' +
        str(followers))
    counts=[]
    for follower in followers:
        count=len(get_followers(oauth, follower))
        counts.append(count)
        print('Found ' + str(count) + ' followers for user ' + follower)
    write_counts(counts)
    return followers

def write_counts(counts):
    with open('gnuplot.dat', 'w') as f:
        for count in sorted(counts):
            f.write(str(count) + ' ' + str(count) + '\n')

if __name__ == "__main__":
    oauth = get_oauth()
    target=parse_arguments()
    l=twitter_search(oauth, target)
    friendCounts=array(l)
    print('Average: ' + str(numpy.mean(friendCounts)))
    print('Std deviation: ' + str(numpy.std(friendCounts)))
    print('Median: ' + str(numpy.median(friendCounts)))
