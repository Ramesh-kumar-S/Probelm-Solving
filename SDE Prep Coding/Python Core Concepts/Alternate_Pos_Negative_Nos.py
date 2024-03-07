# Arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
Arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
Pos = [x for x in Arr if x>=0]
Neg = [y for y in Arr if y<0]
Res=[]
    
for i in zip(Pos,Neg):
    Res.append(i[0])
    Res.append(i[1])

# print("Input Array : ",Arr)    
# print("Output Array : ",Res)
