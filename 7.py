import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Python"

response = requests.get(url)

souped = BeautifulSoup(response.text, "html.parser")

for link in souped.find_all('a'):
    print(link.get("href"))

