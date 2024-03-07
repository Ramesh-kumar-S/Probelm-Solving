import random
import keyboard
import time
from datetime import datetime

def 
def waiting_game():
    Waiting_Time = random.randint(2,4)
    print(f'Your target time is {Waiting_Time} seconds')
    print("---Press Enter to Begin---")
    Started_Time = datetime.now()
    
    time.sleep(Waiting_Time)
    
    print("---Press Enter to Begin---")
    keyboard.on_press("enter",waiting_game)
    
while True:
    waiting_game()
