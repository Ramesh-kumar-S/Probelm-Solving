def selectionSort(items):
    """
    - Only 1 Exchange will occur for every pass
    - During each pass, Maximum element will be placed in their appropriate location
    
    - Approach 1 : Using Max function 
    - Approach 2 : without using Max Function
    """
    for i in range(len(items)-1):
        MaxElement = max(items[0:len(items)-i])
        MaxElementIndex = items.index(MaxElement)
        items[MaxElementIndex] , items[len(items)-i-1] = items[len(items)-i-1], items[MaxElementIndex]
    



alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)

"""
- Approach 2 : without using Max Function
"""
def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)
