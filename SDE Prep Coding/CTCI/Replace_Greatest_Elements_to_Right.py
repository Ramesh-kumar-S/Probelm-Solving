# arr = [17,18,5,4,6,1]
arr = [400]
for index,num in enumerate(arr):
    print(index,arr[index+1:])
    if index !=  len(arr)-1:
        arr[index] = max(arr[index+1:])
#         if len(arr[index+1:]) != 1:
#             arr[index] = max(arr[index+1:])
# #             arr[index] = -1
#         else:
#             arr[index] = -1
    else:
        print(index,len(arr)-1)
        arr[index] = -1

print(arr)