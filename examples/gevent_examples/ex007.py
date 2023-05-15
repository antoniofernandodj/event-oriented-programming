import gevent
from geventhttpclient import HTTPClient

def fetch(url):
    client = HTTPClient.from_url(url)
    response = client.get('/')
    print(f"Fetched {url}, status code: {response.status_code}")
    client.close()

# Create greenlets for parallel HTTP requests
greenlets = [
    gevent.spawn(fetch, "https://www.example.com"),
    gevent.spawn(fetch, "https://www.google.com"),
    gevent.spawn(fetch, "https://www.openai.com")
]

# Wait for all greenlets to complete
gevent.joinall(greenlets)