import os
import threading
import multiprocessing

# Function that runs forever


def cpu_waster():
    while True:
        pass


if __name__ == "__main__":
    print(f'Process ID : {os.getpid()}')
    print(f'Thread Count : {threading.active_count()}')

    # Print the individual threading information
    for thread in threading.enumerate():
        print(thread)

    # Let's start the individual 12 process
    for i in range(15):
        process = multiprocessing.Process(target=cpu_waster)
        # thread = threading.Thread(target=cpu_waster)
        process.start()
        print(f'Processs {i} PID : {process.pid}')

    print(f'Post init - Process ID : {os.getpid()}')
    print(f'Post init - Thread Count : {threading.active_count()}')

    # Print the individual threading information
    for thread in threading.enumerate():
        print(thread)
