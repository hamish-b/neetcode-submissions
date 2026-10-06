class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # given a point i in the array, we can pick the minimum price so far at which to purchase, and then sell at any future time
        if len(prices) == 1:
            return 0
        running_min = prices[0]
        max_profit = max(0, prices[1] - running_min)

        for i in range(1, len(prices) - 1):
            running_min = min(prices[i], running_min)
            iter_profit = prices[i+1] - running_min
            if iter_profit > max_profit:
                max_profit = iter_profit
        
        return max_profit