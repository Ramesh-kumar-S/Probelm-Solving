Arr = [5, 3, 2, 4, 3]
Arr= [4, 3, 6, 2, 1, 1]

Dict = {Arr.count(x):x for x in Arr}
Absent_Elem=[]

# Absent_Elem.append(abs(len(nums) * (len(nums)+1) // 2 - sum(nums)))
for X in range(1,len(Arr)+1):
    if X not in Arr:
        Absent_Elem.append(X)
        break
try:
    Repeating_No = Dict[2]
except KeyError:
    pass
    
print([Repeating_No, *Absent_Elem])