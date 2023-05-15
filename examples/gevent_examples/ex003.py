import gevent
from gevent import monkey

# Monkey patching the standard library to enable cooperative multitasking
monkey.patch_all()


def task(name):
    i = 0
    while i < 5:
        print(f'Task {name} - Iteration {i}')
        gevent.sleep(1)
        i += 1

# Create greenlets for each task
greenlets = [
    gevent.spawn(task, 'A'),
    gevent.spawn(task, 'B'),
    gevent.spawn(task, 'C')
]

# Wait for all greenlets to complete
gevent.joinall(greenlets)