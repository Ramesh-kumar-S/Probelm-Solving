import os
import threading
import multiprocessing 

#Function that runs forever
def cpu_waster():
    while True:
        pass

print(f'Process ID : {os.getpid()}')
print(f'Thread Count : {threading.active_count()}')

#Print the individual threading information
for thread in threading.enumerate():
    print(thread)

#Let's start the individual 12 threads
for i in range(15):
    thread = threading.Thread(target=cpu_waster)
    thread.start()

print(f'Post init - Process ID : {os.getpid()}')
print(f'Post init - Thread Count : {threading.active_count()}')

#Print the individual threading information
for thread in threading.enumerate():
    print(thread)