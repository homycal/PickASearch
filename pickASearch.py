import requests
import sys
import json

if len(sys.argv)!= 2:
    print("Wrong arguments")
    exit(0)

URL = "https://en.wikipedia.org/w/api.php"
params = {"action":"query", "list": "search", "srsearch": sys.argv[1], "format":"json"}

r = requests.get(URL, params= params)
data = json.loads(r.text)
print (data)
