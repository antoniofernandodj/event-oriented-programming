"""
Using gevent with RxPY can provide cooperative concurrency
and enable non-blocking operations. Here's an example tha
 demonstrates the integration of gevent and RxPY:
"""

from gevent import monkey
monkey.patch_all()

import gevent
from rx import from_iterable, operators

# Create an observable from an iterable
numbers = from_iterable(range(10))

# Define an operator to filter even numbers
even_numbers = numbers.pipe(operators.filter(lambda x: x % 2 == 0))

# Subscribe to the filtered observable using gevent
subscription = even_numbers.subscribe(lambda value: print(value))

# Run the event loop with gevent
try:
    gevent.wait()
except KeyboardInterrupt:
    subscription.dispose()

"""
In this example, the monkey.patch_all() call from the gevent library is used to patch
certain standard library functions and enable cooperative concurrency.

The code creates an observable sequence numbers from an iterable (range of numbers from 0 to 9).
The filter operator is then applied to filter out the even numbers.

To subscribe to the filtered observable using gevent, the subscribe method is invoked with a
lambda function that prints each value.

The event loop is run using gevent.wait(), which allows the code to listen for and process
events in a cooperative manner. The subscription is disposed of in case of a keyboard interrupt
(Ctrl+C) to ensure proper cleanup.

By combining gevent's cooperative concurrency model with the reactive programming
capabilities of RxPY, you can achieve non-blocking and event-driven programming.
"""