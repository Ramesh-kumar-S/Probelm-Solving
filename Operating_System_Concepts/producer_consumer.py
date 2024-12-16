import threading
import time
import random
from queue import Queue

# Queue size
BUFFER_SIZE = 5

# Initialize the queue
buffer = Queue(maxsize=BUFFER_SIZE)

# Producer function


def producer():
    while True:
        item = random.randint(1, 100)  # Produce an item
        buffer.put(item)  # Put item into the buffer
        print(f"Produced: {item}")
        time.sleep(random.uniform(0.1, 1))  # Simulate production time

# Consumer function


def consumer():
    while True:
        item = buffer.get()  # Get an item from the buffer
        print(f"Consumed: {item}")
        buffer.task_done()  # Notify the queue that the task is done
        time.sleep(random.uniform(0.1, 1))  # Simulate consumption time


# Create producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start threads
producer_thread.start()
consumer_thread.start()

# Join threads (optional, but keeps the program running)
producer_thread.join()
consumer_thread.join()
