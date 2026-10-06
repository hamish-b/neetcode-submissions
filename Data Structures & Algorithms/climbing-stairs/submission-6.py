class Solution:
    def climbStairs(self, n: int) -> int:
        
        # for n = 1 can climb it one way
        # for n = 2 can climb it two ways
        # for n = 3 (s(2) + s(1) ways) since we can choose to either step once or   step twice initially
        # Hence s(n) = s(n-1) + s(n-2) with s(1) = 1, s(2)

        memo = [-1]*n
        memo[0] = 1
        if n >= 2:
            memo[1] = 2

        def climb_rec(n, memo):

            if memo[n-1] != -1:
                return memo[n-1]
            
            memo[n-1] = climb_rec(n-1, memo) + climb_rec(n-2, memo)

            return memo[n-1]
        
        return climb_rec(n, memo)
