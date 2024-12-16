def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        print(arr[i:])
        Min_Num = arr.index(min(arr[i:]))
        arr[i], arr[Min_Num] = arr[Min_Num], arr[i]
    return arr

arr = [17, 6, 8, 10, 12]
print(selection_sort(arr))


