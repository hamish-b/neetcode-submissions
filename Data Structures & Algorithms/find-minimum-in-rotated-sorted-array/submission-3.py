class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        if r < 2:
            return min(nums)

        if nums[l] < nums[l+1] < nums[r]:
            return nums[0]

        while l<=r:
            
            if r - l <= 2:
                return min(nums[l], nums[l+1], nums[r])

            m = (l+r)//2

            if nums[l] <= nums[l+1] <= nums[m]:
                l = m + 1
            else:
                r = m
            

        