#!/bin/python3
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
import urllib
from urllib.parse import urlparse

CONSUMER_KEY = "dbr6Ce0ahKsr4QMyIxElQ"
CONSUMER_SECRET = "Bxd17G6TSr74lDzpGkl9ThQRqE5HwDtrPofdJninKLA"
OAUTH_TOKEN = "589075411-qVWno21brc3Kjw24Wg6UeDJVHBE6DsrRbd7r0gGU"
OAUTH_TOKEN_SECRET = "fLEC8DJvPqginylDhhCm0F9xNS2R6Xc8djk6DbVlVI"

SEARCH_TERMS = ['carmack','mayweather','canelo','manziel','pasquale','garcia','nascar','football','insiduous','korra','yom kippur','tupac','navy','yard','washington','post','concordia','saints','seahawks','peyton','cowboys','eagles','penn','mileycyrus','ootd','onedirection','selfie','travel','beach','nerd','recipe','fashion','summer','apple','news','java','syria','shooter','obama','world','xtreme','lifestyle','new york','sheen','diet','fitness','jersey','blues','music','guitar','sing','game','facebook','lcot','teaparty','obama2012','breakingbad','batman','rickross','anime','china','iphone','japan','india','books','dinosaur','velociraptor','sauce','google']

def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

def save_links(list):
    file = open('links.txt', 'w')
    for item in list:
        file.write("%s\n" % item)

def twitter_search(oauth, uri_list, suffix):
    for term in SEARCH_TERMS:
        r = requests.get(url='https://api.twitter.com/1.1/search/tweets.json?q=' + suffix + term + '&filter%3Alinks&count=1000', auth=oauth)
        for status in r.json()['statuses']:
            for url in status['entities']['urls']:
                if len(uri_list) == 1000:
                    return
                if 'expanded_url' in url:
                    uri = url['expanded_url']
                    try:
                        r=requests.get(uri)
                        if r.status_code == 200 and not r.url in uri_list:
                            uri_list.add(r.url)
                            print('Added uri: ' + r.url + ' #' + str(len(uri_list)))
                    except requests.exceptions.ConnectionError as e:
                        continue
                    except UnicodeEncodeError as e:
                        continue
                    except IOError as e:
                        continue


if __name__ == "__main__":
    oauth = get_oauth()
    uri_list = set()
    twitter_search(oauth, uri_list, '')
    twitter_search(oauth, uri_list, '%23')
    print(uri_list)
    print('List length: ' + str(len(uri_list)) + ' from ' + str(len(SEARCH_TERMS)) + ' terms')
    save_links(uri_list)
