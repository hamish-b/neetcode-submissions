class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        # work backwards
        
        m = len(grid)
        n = len(grid[0])

        memo = [[-1 for _ in range(n)] for _ in range(m)]
        memo[0][0] = grid[0][0]

        def min_sum_rec(d, r, memo):
            if memo[d][r] != -1:
                return memo[d][r]
            elif d == 0:
                memo[d][r] = min_sum_rec(d, r-1, memo) + grid[d][r]
                return memo[d][r]
            elif r == 0:
                memo[d][r] = min_sum_rec(d-1, r, memo) + grid[d][r]
                return memo[d][r]
            else:
                memo[d][r] = min(min_sum_rec(d-1, r, memo), min_sum_rec(d, r-1, memo)) + grid[d][r]
                return memo[d][r]
        return min_sum_rec(m-1, n-1, memo)

        