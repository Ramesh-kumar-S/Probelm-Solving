arr = [1,2,34,3,4,5,7,23,12]
arr = [1,1,1]
def Odd(arr):
    Count=0
    for i in arr:
        if Count == 3:
            return True
        if i%2 != 0:
            Count += 1
        else:
            Count=0
    return False 
print(Odd(arr))