import tracemalloc

def max_profit(prices):
    max_profit_amt = 0
    min_price = float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit_amt = max(max_profit_amt, profit)
    return max_profit_amt

tracemalloc.start()
# Example usage:
prices = [7, 1, 5, 3, 6, 4]
result = max_profit(prices)
print(f"The maximum profit is: {result}")
print(tracemalloc.get_traced_memory())
print(tracemalloc.stop())


