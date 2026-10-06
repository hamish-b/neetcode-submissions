class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        list_of_triplets = []

        # implement two sum with two pointers for each element in the list 
        
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -1 * nums[i]
            l, r = i + 1, len(nums) - 1

            while l < r:

                iter_sum = nums[l] + nums[r]

                if iter_sum == target:
                    list_of_triplets.append([nums[i], nums[l], nums[r]]) 

                if iter_sum > target:
                    r += -1
                else:
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return list_of_triplets