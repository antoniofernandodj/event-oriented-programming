import gevent
from gevent import lock

semaphore = lock.Semaphore(value=2)

def task(name):
    with semaphore:
        print(f'{name} acquired semaphore')
        gevent.sleep(1)
    print(f'{name} released semaphore')

# Create greenlets for tasks
greenlets = [
    gevent.spawn(task, 'A'),
    gevent.spawn(task, 'B'),
    gevent.spawn(task, 'C'),
    gevent.spawn(task, 'D')
]

# Wait for all greenlets to complete
gevent.joinall(greenlets)