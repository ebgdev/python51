def maxProfit(prices) -> int:
        min_price = float('inf')  # start with the highest possible value
        profit = 0
        for value in prices:
            # update the minimum price seen so far
            if value < min_price:
                min_price = value
            # update profit if selling today is better
            elif value - min_price > profit:
                profit = value - min_price
        return profit