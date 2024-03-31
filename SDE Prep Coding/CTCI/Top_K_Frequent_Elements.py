from collections import Counter

Arr = [1,1,1,2,2,3]
Arr = [1]
K=2


Elem = [x[0] for x in list(Counter(Arr).most_common(1))]
print(Elem)
