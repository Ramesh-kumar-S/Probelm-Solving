"""
                        Greedy Approach , 
        Since we're sorting the Array in Decreasing order 
        Inorder to pick up the Higher value coing first(which is locally optimal)

"""
def MinimumCoins(target, coins):
    Coin_Count = 0
    values = []
    for coin in reversed(sorted(coins)):
        while target >= coin:
            target-=coin
            values.append(coin)
            Coin_Count+=1
    print(Coin_Count)
    print(sum(values))
    return Coin_Count


# MinimumCoins(13,[5, 2, 4])

