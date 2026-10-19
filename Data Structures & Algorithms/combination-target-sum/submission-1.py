class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # so we try to use the first integer which gives us a new target (target - nums[0])
        # if this fails we try using the second integer and so on

        def sumRec(target, nums, curr, sols):

            for i in range(len(nums)):

                new = curr + [nums[i]]

                if target - nums[i] == 0:
                    sols.append(new)

                if target - nums[i] > 0:
                    sumRec(target - nums[i], nums[i:], new, sols)
        
        curr = []
        sols = []
        sumRec(target, nums, curr, sols)
        return sols