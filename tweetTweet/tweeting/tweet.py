'''
@author: benpetroski
'''

from urllib2 import Request, urlopen, URLError
from pprint import pprint
from xml.dom import minidom
import requests, json, twitter

class kitty(object):
    def text(self):
        try:
#             response = urlopen(Request('http://placekitten.com'))
#             kitty = response.read()
            kitty = requests.get('http://placekitten.com')
            print kitty.text[560:1050]
        except URLError, e:
            print 'No kitties. Error: ', e
    def pic(self):
        kittens = urlopen('http://placekitten.com/201/300')
        f = open('kitty.jpg', 'wb')
        f.write(kittens.read())
        f.close()
        
def hk():
    try:
        hk = requests.get('http://thehofmeisterkink.com')
        print hk.headers
    except URLError, e:
        print 'No kitties. Error: ', e

def pets():
    f = open('pets.txt', 'r')
    pets = minidom.parseString(f.read())
    f.close()
    
    names = pets.getElementsByTagName('name')
    for name in names:
        print name.firstChild.nodeValue

def pets2():
    f = open('pets2.txt', 'r')
    pets = json.loads(f.read())
    f.close()
    
    pprint(pets)

def bitly():
    query_params = {'access_token': 'API_KEY',
                'link': 'http://bit.ly/1hrUPUa',
                'unit': 'minute',
                'units': 15}

    endpoint = 'https://api-ssl.bitly.com/v3/link/referrers'
    response = requests.get(endpoint, params= query_params)
    
    data = json.loads(response.content)
    print data

def bnptrsk_tweetTweet():
    API_KEY='***'
    endpoint='https://api.twitter.com/1.1/statuses/update.json'
    
    api = twitter.Api()
    print api

if __name__ == '__main__':
    bnptrsk_tweetTweet()
    


    
    