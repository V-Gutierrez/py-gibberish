import requests
import sys

api_url = "http://shibe.online/api/shibes"

x = requests.get(api_url, params={"count": 5})

print(x.content)
