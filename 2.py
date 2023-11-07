import requests

s1 = "https://archlinux.org/"
s2 = "https://requestb.in"

try:
    response = requests.get(s2)
    print(response.text)
except Exception as e:
    print(e)

