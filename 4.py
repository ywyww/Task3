import requests

domain = "https://ru.wikipedia.org/"
filename = "robots.txt"
url = domain + filename

text = requests.get(url).text

print(text)
