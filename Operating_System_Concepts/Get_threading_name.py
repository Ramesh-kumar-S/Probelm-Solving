import threading
import os
import time

is_purification_enabled = True
def purify_water():
    name = threading.current_thread().getName()
    purify_count = 0
    while is_purification_enabled:
        print(f'{name} is purifying the water')
        purify_count+=1
    print(f'End : {name} has purified the {purify_count} particles in 3 secs!')

#Gaurd is mandatory
if __name__ == "__main__":
    thread1 = threading.Thread(target=purify_water, name="PureIT")
    thread2 = threading.Thread(target=purify_water, name="Marvella")
    
    #Start the thread
    thread1.start()
    thread2.start()
    
    time.sleep(1)
    is_purification_enabled=False #Turf off the purifier
    
        
    