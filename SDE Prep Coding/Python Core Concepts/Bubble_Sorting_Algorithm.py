"""
BUBBLE SORTING AlGORITHM
"""
def bubbleSort(items):
    for item in range(len(items)-1, 0, -1):
        for i in range(item):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
    return items

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)


"""
OPTIMIZED BUBBLE SORTING AlGORITHM
"""
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)
