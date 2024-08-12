from collections import Counter
arr = ["d","b","c","b","c","a"]
arr = ["aaa","aa","a"]
k=1
#Ordered Dict can be used to preserve order 
counter = dict(Counter(arr))
c=0
for i in arr:
    if i in counter:
        if counter[i] == 1:
            c+=1
    if c == k:
        print(i)
