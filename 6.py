from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/Main_Page"

response = urlopen(url)
souped = BeautifulSoup(response.read(), 'html.parser')

print(*souped.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "h7"]), sep='\n')
