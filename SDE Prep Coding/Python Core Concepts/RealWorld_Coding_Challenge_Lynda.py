import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
 
#Progress Bar    
N=10
for i in range(N):
    # print("\n\n\n")
    print(" " * i + "*")
    R=N-i
    R+=1
    print(" " * R + "*")
    
    # time.sleep(1)
    # clear()
    
    #Reverse Diagonal from Right Side
    # R=N-i
    # print(" " * R + "*")

A=[["" for y in range(5)] for x in range(5)]

# for i in reversed(range(0,20)):
#     print(" " * i + "*")

# Alpha="abcdefghijklmnopqrstuvwxyz"
# print(Alpha[:5])

# N=3
# for i in range(N):
#     print("-"*)