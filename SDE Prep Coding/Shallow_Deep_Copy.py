import copy

#Deep Copy and Shallow Copy

#Shallow Copy
A=[1,2,3,4,5,6]
B=A
# print(B)
B.append(9)
# print(B)
# print(A)


#Deep Copy
A=[1,2,3,4,5,6]
B=copy.deepcopy(A)
print(B)
B.append(9)
print(B)
print(A)