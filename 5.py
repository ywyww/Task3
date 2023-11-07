import requests
from bs4 import BeautifulSoup

url = "http://www.example.com/"

response = requests.get(url)

souped = BeautifulSoup(response.text, 'html.parser')

print(souped.h1)