import gevent
import requests

results = []

urls = [
    "https://www.google.com",
    "https://www.openai.com"
]

def fetch(url):
    response = requests.get(url)
    results.append(response)
    print(f"Fetched {url}, status code: {response.status_code}")

greenlets = [gevent.spawn(fetch, url) for url in urls]

gevent.joinall(greenlets)

print(results)