import threading
import time

"""
Data Race :
        2 or More concurrent threads access the same memory location.
        
        Using the Mutual Exclusion to implement lock based mechanism to protect the critical section.
        
        Mutex Lock Mechanism has been used to implement the Mutual Exclusion.
"""
stock = 0
market = threading.Lock()


def stocks_count():
    global stock
    
    for i in range(6):
        print(f'{threading.current_thread().name} is working on the stocks.')
        time.sleep(0.5)
        market.acquire()
        stock += 1
        market.release()


if __name__ == "__main__":
    SDE = threading.Thread(target=stocks_count)
    MTS = threading.Thread(target=stocks_count)

    SDE.start()
    MTS.start()
    time.sleep(3)
    SDE.join()
    MTS.join()

    print(f'Final Stock count : {stock}')
