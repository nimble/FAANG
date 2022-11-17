# Sliding Window 


# i represents days
def maxProfit(prices):
    # prices = [7,6,4,3,1]
    # Let's find the min number first out of the array..
    low_num = -1
    profit = 0
    for num in prices:
        if num > low_num:
            low_num = num
    # This will give us the smallest num.



