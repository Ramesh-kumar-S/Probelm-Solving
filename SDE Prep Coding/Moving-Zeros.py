Arr = [0,1,0,3,12]
Arr = [2,1]

Zeros=Arr.count(0)
for i in range(Zeros):
    Arr.remove(0)
for i in range(Zeros):
    Arr.append(0)
print(Arr)


