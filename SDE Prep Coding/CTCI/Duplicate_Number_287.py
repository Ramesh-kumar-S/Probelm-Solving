from collections import  Counter
Arr =  [1,3,4,2,2]

# for Key,Value in sorted(Counter(Arr).items()):
#     if Value == 2:
#         print(Key)
#         break

Duplicate_Num = set()
for Num in Arr:
    if Num in Duplicate_Num:
        print(Num)
        break 

    Duplicate_Num.add(Num)