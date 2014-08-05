'''
@author: benpetroski
'''

from urllib2 import Request, urlopen, URLError

class kitty(object):
    def text(self):
        try:
            response = urlopen(Request('http://placekitten.com'))
            kitty = response.read()
            print kitty[560:1050]
        except URLError, e:
            print 'No kitties. Error: ', e
    def pic(self):
        kittens = urlopen('http://placekitten.com/201/300')
        f = open('kitty.jpg', 'wb')
        f.write(kittens.read())
        f.close()
        
def hk():
    try:
        response = urlopen(Request('http://thehofmeisterkink.com'))
        hk = response.read()
        print hk
    except URLError, e:
        print 'No kitties. Error: ', e

if __name__ == '__main__':
    k=kitty()
    k.text()
    hk()

    
    