arr = [1, 5, 5, 25, 125]
r = 5

Res=[]
# IndexMap = { K: arr.index(K) for K in arr }
IndexMap = {arr.index(K) : K for K in arr}
print(IndexMap)

# Init = 0
# for i in range(len(arr)):
#     Init = arr[i]
#     Second = Init*r
#     Third = Second*r
#     print(i, Init, Second, Third)
#     if Init in IndexMap.values() and Second in IndexMap.values() and Third in IndexMap.values():
#         temp = (IndexMap[Init], IndexMap[Second], IndexMap[Third])
#         Res.append(temp)

# print(Res)

