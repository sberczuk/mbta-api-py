import requests
import json

r = requests.get('https://api-v3.mbta.com/stops', headers={'Accept': 'application/vnd.api+json'})

data = r.json()


for stop in data.get('data'):
    print(stop['id'])
