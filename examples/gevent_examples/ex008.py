import gevent
from gevent import Timeout
import requests

def fetch_with_timeout(url, timeout):
    try:
        with Timeout(timeout):
            response = requests.get(url)
            print(f"Fetched {url}, status code: {response.status_code}")
    except Timeout as e:
        print(f"Timeout occurred while fetching {url}")

# Create greenlets for fetching URLs with timeouts
greenlets = [
    gevent.spawn(fetch_with_timeout, "https://www.google.com", 3),
    gevent.spawn(fetch_with_timeout, "https://www.openai.com", 10)
]

# Wait for all greenlets to complete
gevent.joinall(greenlets)