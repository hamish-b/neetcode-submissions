class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins.sort()
        inf = float('inf')
        dp = [0] + [inf] * amount

        for a in range(amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a-c] + 1, dp[a])
        if dp[amount] < inf:
            return dp[amount]
        else:
            return -1
            