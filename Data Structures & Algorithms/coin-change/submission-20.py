class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = [0] + [amount+1] * (amount)

        def ccRec(coins, a, memo):
            
            if memo[a] != amount+1:
                return memo[a]

            candidates = [1 + ccRec(coins, a - coins[i], memo) for i in range(len(coins)) if coins[i] <= a]

            if len(candidates) == 0:
                return memo[a]

            memo[a] = min(candidates)
            return memo[a]
        ans = ccRec(coins, amount, memo)
        if ans < amount + 1:
            return ans
        else:
            return -1