class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # given a point i in the array, we can pick the minimum price so far at which to purchase, and then sell at any future time
        if len(prices) == 1:
            return 0
        running_min = prices[0]
        running_max = max(prices[1:])
        max_profit = max(0, running_max - running_min)

        for i in range(1, len(prices) - 1):
            running_min = min(prices[i], running_min)
            if prices[i] == running_max:    
                running_max =  max(prices[i+1:])
            iter_profit = running_max - running_min
            if iter_profit > max_profit:
                max_profit = iter_profit
        
        return max_profit