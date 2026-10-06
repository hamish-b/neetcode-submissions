class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        list_of_triplets = []

        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1

            while l < r:
                iter_sum = num + nums[l] + nums[r]

                if iter_sum == 0:
                    list_of_triplets.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
                elif iter_sum > 0:
                    r -= 1
                else:
                    l += 1
                
            
        return list_of_triplets


            