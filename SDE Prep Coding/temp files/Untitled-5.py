d={8:"Eight",1: 'one', 2: 'two', 3: 'three', 4: 'four'}
# print(d.pop(1,"Not Found"))
# print(d.popitem())
# print(sorted(d.items()))
# c=d.copy()
# print("Hey",c)
# # print(d.popitem())
# print(d)
# print(d.get(2))
# # print(d.keys()); print(d.values()); print(d.items())
# # print(d.max())

# print(max(d,key=d.get))

import json
D={"SDE":["Apple","Google","Microsoft"],"SRE":["Adobe","LinkedIn"],"Computer Scientist":["Adobe","Microsoft"]}

D["SDE"].append("LinkedIN")
print(json.dumps(D,indent=4))
for K,V in D.items():
    print(K,V,sep="-")
    for Val in V:
        print(Val)
