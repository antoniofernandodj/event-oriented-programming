import gevent
import gevent.socket as socket

def connect(host, port):
    socket.create_connection((host, port), timeout=5)
    print(f"Connected to {host}:{port}")

# Create greenlets for connecting to multiple hosts
greenlets = [
    gevent.spawn(connect, "www.example.com", 80),
    gevent.spawn(connect, "www.google.com", 80),
]

# Wait for all greenlets to complete or timeout after 10 seconds
gevent.joinall(greenlets, timeout=10)