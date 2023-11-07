import requests


url = "https://python.org"
response = requests.get(url)

print(f"Status code {response.status_code}",
      f"Headers {response.headers}",
      f"Url {response.url}",
      f"History {response.history}",
      f"Encoding {response.encoding}",
      f"Reason {response.reason}",
      f"Cookies {response.cookies}",
      f"Elapsed {response.elapsed}",
      f"Request {response.request}",
      f"Content {response.content}",
      sep='\n'
      )