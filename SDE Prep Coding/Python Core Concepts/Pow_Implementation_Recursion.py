N=5

def Pow(Value, power):  # sourcery skip: assign-if-exp
    # return 1 if power == 0 else (N*Pow(N,power-1))
    print(Value, power)
    if power in [0, 1]:
        return 1
    if power < 0:
        pass
    else:
        return (Value*Pow(Value,power-1))

# print(Pow(2.0000,-2))


string = "aaabccddd"
# print(len(string))
indices = []
for s in range(len(string)-1):
    if string[s] == string[s+1]:
        pass
        # string = string[s+1:]
        # print(string[s+1:])
    # print(string[s],string[s+1])
    
# Valid Sudok0
from collections import Counter
Arr = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

#Check Rows Non-Repeating 1-9 Chars
Cols = []
for row in Arr:
    #Validating Columns
    if row[0] != ".":
        Cols.append(row[0])
    #Validating Rows
    for value,count in Counter(row).items():
        if count>1 and value != ".":
            print(value)

# 3X3 Validation
for num in range(3):
    for r in range(3):
        pass
        # print(Arr[num][r])



#SuperReduced String
# a = "aaabccddd"
# Res = ""
# for i in range(0,len(a)-1,2):
#     if a[i] == a[i+1]:
#         print(a[i],a[i+1])
#         continue
#     else:
#         Res+=a[i]
    
s="badc"
t="baba"

mapping = {}
for s1,t1 in zip(s,t):
    mapping[s1]=t1
    # print(s1,t1)
print(mapping)
Res=""
for ss in s:
    Res+=mapping[ss]
print(Res)