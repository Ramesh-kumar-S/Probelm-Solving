Arr = [
    [5,6,1,10],
    [9,20,15,5],
    [2,1,3,7],
    [8,11,8,9]
]

PD=[]
SD=[]
print("Primary Diagonal of the Matrix ")
for i in range(len(Arr)):
    print(Arr[i][i],end=" ")
    PD.append(Arr[i][i])

print("     ")
print("\nSecondary Diagonal of the Matrix ")
for i in range(len(Arr)):
    print(Arr[i][len(Arr)-i-1],end=" ")
    SD.append(Arr[i][len(Arr)-i-1])
print("     ")
    
print(f"\nSum of Primary Diagonal : {sum(PD)}")
print(f"\nSum of Secondary Diagonal : {sum(SD)}")

print(f"\nDifference between Primary & Secondary Diagonal : {sum(PD)-sum(SD)}")


# for i in range(len(Arr)):
#     # print(Arr[i][i])  #Primary Diagonal
#     print(Arr[i][len(Arr)-i-1])

    # print(len(Arr[i])-i)
    # print(Arr[len(Arr)-i])
    # print(Arr[len(Arr)-i][len(Arr)-i])
    