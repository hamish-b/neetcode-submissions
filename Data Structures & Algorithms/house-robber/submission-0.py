class Solution:
    def rob(self, nums: List[int]) -> int:
        
        N = len(nums)

        memo = [-1 for _ in range(N)]
        memo[0] = nums[0]
        if N >= 2:
            memo[1] = max(nums[0], nums[1])

        def rob_rec(nums, memo):

            n = len(nums)
            if memo[n-1] != -1:
                return memo[n-1]
            else:
                memo[n-1] = max(rob_rec(nums[:-1], memo), rob_rec(nums[:-2], memo) + nums[-1])

            return memo[n-1]

        return rob_rec(nums, memo)
        # solution is max(rob(nums[:-4]) + nums[-2], rob(nums[:-3]) + nums[-1])


        