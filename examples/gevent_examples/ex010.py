import gevent
from gevent.queue import Queue

def worker(name, task_queue):
    while not task_queue.empty():
        task = task_queue.get()
        print(f"Worker {name} processing task: {task}")
        gevent.sleep(1)

# Create a task queue
task_queue = Queue()

# Put tasks into the queue
for i in range(5):
    task_queue.put(f"Task {i+1}")

# Create greenlets for workers
greenlets = [
    gevent.spawn(worker, "A", task_queue),
    gevent.spawn(worker, "B", task_queue),
    gevent.spawn(worker, "C", task_queue)
]

# Wait for all greenlets to complete
gevent.joinall(greenlets)