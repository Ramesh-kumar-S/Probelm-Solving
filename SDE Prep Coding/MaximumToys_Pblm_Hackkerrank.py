prices = [1, 2, 3, 4]
prices = [1, 12, 5, 111, 200, 1000, 10]
k = 50


prices.sort()
Res=0
Count=0
for price in prices:
    if price <= k:
        Res += price
        if Res <= k:
            Count+=1

print(Count)
