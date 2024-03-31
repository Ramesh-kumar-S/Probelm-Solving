"""
    Binary Search
    
    Perfrom Binary Search via Naive Approach
    Perform Binary Search via Recursive Approach
"""

Arr=[3,7,8,10,12,14,17]
Target=12

def BinarySearch(Arr: list[int], Target: int):
    low=0
    high=len(Arr)-1

    while low <= high:
        mid=(low+high)//2
        if Arr[mid] == Target:
            return mid
        if Arr[mid] < Target:
            low = mid+1
        else:
            high = mid-1
    return -1
        
print(BinarySearch(Arr, Target))