class Solution:
    def climbStairs(self, n: int) -> int:
        
        # for n = 1 can climb it one way
        # for n = 2 can climb it two ways
        # for n = 3 (s(2) + s(1) ways) since we can choose to either step once or   step twice initially
        # Hence s(n) = s(n-1) + s(n-2) with s(1) = 1, s(2)
        if n == 1:
            return 1
        if n == 2:
            return 2
        table_of_vals = [0 for _ in range(n)]
        table_of_vals[0] = 1
        table_of_vals[1] = 2

        for i in range(2, n):
            table_of_vals[i] = table_of_vals[i-1] + table_of_vals[i-2]

        return table_of_vals[n-1]
