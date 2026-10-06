class Solution:
    def rob(self, nums: List[int]) -> int:
        
        N = len(nums)
        
        if N == 1:
            return nums[0]
        if N == 2:
            return max(nums[0], nums[1])

        prev_val = nums[0]
        current_val = max(nums[0], nums[1]) 
        next_val = None

        for i in range(2, N):
            next_val = max(current_val, prev_val + nums[i])
            prev_val = current_val
            current_val = next_val
        
        return next_val

        