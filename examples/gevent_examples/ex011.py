import gevent
from gevent.event import AsyncResult

def producer(result):
    gevent.sleep(2)
    result.set("Hello, consumer!")

def consumer(result):
    value = result.get()
    print(f"Consumer received: {value}")

# Create an AsyncResult object
result = AsyncResult()

# Create greenlets for producer and consumer
greenlets = [
    gevent.spawn(producer, result),
    gevent.spawn(consumer, result)
]

# Wait for all greenlets to complete
gevent.joinall(greenlets)