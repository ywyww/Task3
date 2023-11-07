from urllib import *
from urllib.request import urlopen 
from urllib.error import HTTPError
from urllib.error import URLError

def print_html(url: str, size: int = 1000) -> None:
    try:
        html: str = urlopen(url)
    except HTTPError:
        print("HTTPError")
    except URLError:
        print("URLError")
    else:
        print(html.read(size).decode("utf-8"))


url = "http://www.afawfawf.com/"
url_1 = "https://en.wikipedia.org/wiki/Althea_Gibson"


print_html(url)
print_html(url_1)
