import itertools
from collections import Counter
Doors = [0 for _ in range(101)]

for i in range(1,101):
    for j in range(i,101,i):
        Doors[j] = 1 if Doors[j] == 0 else 0

print(f'No of Doors which are opened after 100th Pass : {Counter(Doors)[1]}')
# print(Doors)
indices_of_ones = [index for index, value in enumerate(Doors) if value == 1]
print(f'Opened Door Nos : {indices_of_ones}')
    
# Doors_Open = [X for X in range(len(Doors)) if Doors[X]==1]
# print(Doors_Open)

