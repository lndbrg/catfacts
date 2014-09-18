import random
import re
import requests
from lxml.html import soupparser

def catfact():
    tree = soupparser.fromstring(
            requests.get('http://maxellah.tripod.com/catfacts.htm').text
            )
    facts = tree.xpath('//ul/li/text()')
    print (re.sub(r'\s+', ' ', random.choice(facts)))
