from collections import  Counter
nums = [4,3,2,7,8,2,3,1]
Res = [Key for Key, Value in Counter(nums).items() if Value == 2]
print(sorted(Res))