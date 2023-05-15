import gevent
import time
from gevent import event

def task(name, event: event.Event):
    print(f'Task {name} waiting')
    event.wait()
    print(f'Task {name} triggered')

print('# Create an event')
evt = event.Event()

print('# Create greenlets for tasks')
greenlets = [
    gevent.spawn(task, 'A', evt),
    gevent.spawn(task, 'B', evt),
    gevent.spawn(task, 'C', evt)
]

print('# Wait for a few seconds before triggering the event')
gevent.sleep(2)
evt.set()

print('# Wait for all greenlets to complete')
gevent.joinall(greenlets)