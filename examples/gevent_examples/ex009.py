import gevent
import time

def periodic_task(interval):
    while True:
        print("Running periodic task...")
        gevent.sleep(interval)

def other_task(interval):
    while True:
        print("Doing other work...")
        gevent.sleep(interval)

# Start a periodic task that runs every 2 seconds
gevent.spawn_later(0, periodic_task, 2)
gevent.spawn_later(0, other_task, 1)

# Do other work in the main program
while True:
    print('Doing another task..')
    gevent.sleep(5)