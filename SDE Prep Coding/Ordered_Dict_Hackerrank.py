from collections import OrderedDict

Items_DB = OrderedDict()
for _ in range(int(input())):
    Item = input().split()
    Product = " ".join(Item[:-1])
    Price = int(Item[-1])
    if Product in Items_DB:
        Items_DB[Product]+=Price
    else:
        Items_DB[Product]=Price

for K,V in Items_DB.items():
    print("".join(K),V)