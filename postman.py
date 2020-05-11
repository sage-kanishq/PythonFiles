import requests
from pprint import pprint
import json
payload = {
    "title":"Coffee With Karan",
    "author":"Karan Johar",
    "email":"karan.johar@gmail.com"
}

print(requests.request('DELETE','http://localhost:8000/generic/article/2',auth=('kaushik','kaushik')).text)
print(json.dumps(json.loads(requests.request('GET','http://localhost:8000/article/').text),indent=2))