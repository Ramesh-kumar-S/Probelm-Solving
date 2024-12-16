"""
Semaphores are a synchronization mechanism used to control access to a common resource in concurrent programming, ensuring that multiple threads or processes do not access the resource simultaneously in a way that could cause data corruption or inconsistency. They are particularly useful in managing access to limited resources or critical sections in a program.

Types of Semaphores
1. Counting Semaphore:
                        A counting semaphore can take any non-negative integer value. It is used to manage access to a resource that has a limited number of instances.
The semaphore count indicates the number of available resources. If the count is greater than zero, a resource is available, and if it's zero, all resources are currently in use.

2. Binary Semaphore (also known as a Mutex):
                        A binary semaphore can only take the values 0 or 1. It is used to manage access to a single resource or critical section.
It works like a lock, where 1 indicates the resource is available and 0 indicates it is locked or unavailable.

Basic Operations
Semaphores support two primary operations, often called wait and signal (or P and V operations in some literature):

1. Wait (P operation):
    If the semaphore value is greater than zero, decrement it by one and proceed.
    If the semaphore value is zero, the process/thread is put to sleep until the semaphore value is greater than zero.
2. Signal (V operation):
    Increment the semaphore value by one.
    If there are any processes/threads waiting, one is awakened to proceed.
    
Uses:
    - Resources management (Database connection, Network sockets etc,.)
    - Prevents Race condition.
    - Threads are given importance in the ordder they request.
"""
import threading
import time

Semaphore = threading.Semaphore(2)


def worker(num):
    print(f'Worker - {num} is waiting to acquire the semaphore.')
    Semaphore.acquire()
    print(f'Worker -{num} has acquired the critical section.')
    time.sleep(10)
    print(f'Worker - {num} is leaving the critical section.')
    Semaphore.release()


t = []
for i in range(10):
    thread = threading.Thread(target=worker, args=(i,))
    t.append(thread)
    thread.start()

for thread in t:
    thread.join()

print(f'Hurray!! All the workers has completed the jobs.')
