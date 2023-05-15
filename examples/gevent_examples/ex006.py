import gevent
from gevent import pool

def task(name):
    print(f'Task {name} running')
    gevent.sleep(1)
    print(f'Task {name} completed')

# Create a thread pool with a maximum of 2 worker threads
thread_pool = pool.Pool(2)

# Add tasks to the thread pool
for i in range(5):
    thread_pool.spawn(task, i)

# Wait for all tasks to complete
thread_pool.join()