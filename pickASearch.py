import requests
import sys
import json
import random

if len(sys.argv)!= 2:
    print("Wrong arguments")
    exit(0)

URL = "https://en.wikipedia.org/w/api.php"
sroffset="1"
#First request
params = {"action":"query", "list": "search", "srsearch": sys.argv[1], "format":"json", "srlimit":"1", "sroffset":sroffset}
r = requests.get(URL, params= params)
data = json.loads(r.text)
query = data['query']

maxi = query['searchinfo']['totalhits'] -1
if(maxi > 9999) :
    maxi = 9999
sroffset = random.randint(0,maxi)

#Second request
params = {"action":"query", "list": "search", "srsearch": sys.argv[1], "format":"json", "srlimit":"1", "sroffset":sroffset}
r = requests.get(URL, params= params)
data = json.loads(r.text)
query = data['query']

#Display
for page in query['search']:
    print (page['title'] + " : https://en.wikipedia.org/wiki/" + page['title'].replace(" ","_"))
