import requests
import json

url = "http://api.geonames.org/searchJSON?q=Western+Province&country=LK&featureClass=P&maxRows=50&username=chanuka.dev"

payload = ""
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
# print(response.text)

response_data = json.loads(response.text)
cities = [entry['name'] for entry in response_data['geonames']]


print(len(cities))
