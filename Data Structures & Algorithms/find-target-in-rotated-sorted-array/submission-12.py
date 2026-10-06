class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) <= 2:
            if nums[0] == target:
                return 0
            elif len(nums) == 2 and nums[1] == target:
                return 1
            else: 
                return -1

        l, r = 0, len(nums) - 1

        while l < r:

            m = (l+r) // 2

            if r - l <= 2:
                if nums[l] <= nums[l+1] and nums[l] <= nums[r]:
                    pivot = l
                    break
                elif nums[l+1] <= nums[l] and nums[l+1] <= nums[r]:
                    pivot = l+1
                    break
                else:
                    pivot = r
                    break

            if nums[l] <= nums[l+1] <= nums[m]:
                l = m + 1
            elif nums[m] <= nums[m+1] <= nums[r]:
                r = m 
        
        # now we sort and perform a binary search on each sides of the pivot as these are each sorted arrays
        l, r = 0, pivot - 1

        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        l, r = 0, len(nums) - pivot - 1

        while l <= r:
            m = (l+r) // 2
            if nums[pivot + m] == target:
                return m + pivot
            elif nums[pivot + m] < target:
                l = m+1
            else:
                r = m-1
        
        return -1

            
            
        