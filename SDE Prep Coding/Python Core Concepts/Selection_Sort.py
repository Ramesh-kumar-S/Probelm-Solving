#Selection Sort
"""
    Selection Sort - Start from i to N-1 and 
                     Swap ith element to the Min value from [i:n-1]
"""

Arr=[4,3,9,6,1,7,0]

for Num in range(len(Arr)):
    Min_Ith_index=min(Arr[Num:])
    Index=Arr.index(Min_Ith_index)
    Arr[Num], Arr[Index] = Arr[Index], Arr[Num]

print(Arr)