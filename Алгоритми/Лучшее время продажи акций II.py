def maxProfit(prices):
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    return max_profit

print(maxProfit([7, 1, 5, 3, 6, 4]))  
print(maxProfit([1, 2, 3, 4, 5]))     
print(maxProfit([7, 6, 4, 3, 1]))
     
