#!/bin/python3
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urllib.parse import urlparse

CONSUMER_KEY = "dbr6Ce0ahKsr4QMyIxElQ"
CONSUMER_SECRET = "Bxd17G6TSr74lDzpGkl9ThQRqE5HwDtrPofdJninKLA"
OAUTH_TOKEN = "589075411-qVWno21brc3Kjw24Wg6UeDJVHBE6DsrRbd7r0gGU"
OAUTH_TOKEN_SECRET = "fLEC8DJvPqginylDhhCm0F9xNS2R6Xc8djk6DbVlVI"

SEARCH_TERMS = ['carmack','Mayweather','Canelo','Manziel','Pasquale','Garcia','NASCAR','Football','Insiduous','Korra','Yom Kippur','Tupac']


def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

if __name__ == "__main__":
    oauth = get_oauth()
    uri_list = set()
    for term in SEARCH_TERMS:
        r = requests.get(url='https://api.twitter.com/1.1/search/tweets.json?q=' + term, auth=oauth)
        for status in r.json()['statuses']:
            for url in status['entities']['urls']:
                if 'expanded_url' in url:
                    uri_list.add((urlparse(url['expanded_url']).netloc))
    print(uri_list)
