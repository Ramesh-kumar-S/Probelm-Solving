import threading
import time

def print_10_numbers():
    for i in range(10):
        print(f'T1 - {i}')
        time.sleep(1)

def print_20_numbers():
    for i in "RameshKumarSekar-MTS NetApp":
        print(f'T2 - {i}')
        time.sleep(1)

"""
Explanation:
1. Thread Creation:
Two threads are created using the threading.Thread class. Each thread is associated with a target function (print_numbers and print_letters).

2. Thread Start:
The start() method is called on each thread to begin execution. This will cause each thread to run its target function concurrently.

3. Thread Join:
The join() method is called on each thread to wait for them to finish execution. This ensures that the main program waits for both threads to complete before proceeding.
"""
#Thread is  created and Threads will be in  "New" State
Thread1 = threading.Thread(target=print_10_numbers)   
Thread2 = threading.Thread(target=print_20_numbers)

#Thread is in Running state.
Thread1.start()
Thread2.start()

#Thread is Waiting State, to get all the threads completed.
Thread1.join()
Thread2.join()