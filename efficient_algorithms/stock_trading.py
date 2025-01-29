# You are given the price of a stock for n days.
# Your task is figure out the highest profit you could 
# have made if you had bought the stock on one day and sold it on another day.

import time

def best_profit(prices):
    min_price = float("inf")
    best = 0

    for price in prices:
        min_price = min(min_price, price)
        best = max(best, price - min_price)
    return best

def best_profit2(prices):
    n = len(prices)
    best = 0
    for i in range(n):
        for j in range(i + 1, n):
            best = max(best, prices[j] - prices[i])
    return best

numbers = [2, 4, 5, 4, 2, 4, 8, 7, 5]
start_time = time.time()
result = best_profit2(numbers)
end_time = time.time()

print("result", result)
print("time:", round(end_time - start_time, 2), "s")