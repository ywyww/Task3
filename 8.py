import requests 

url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.csv"
response = requests.get(url)

print(response.text.count('\n'))
