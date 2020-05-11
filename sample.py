import requests
import json
response = requests.get("https://reqres.in/")

print(json.dumps(dict(response.request.headers),indent=2))



