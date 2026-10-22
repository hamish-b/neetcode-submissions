class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1.sort()
        nums2.sort()

        intersection = set()

        for num in nums1:

            l, r = 0, len(nums2) - 1

            while l <= r:

                mid = (l+r) // 2

                if num == nums2[mid]:
                    intersection.add(num)
                    break
                elif nums2[mid] > num:
                    r = mid - 1
                else:
                    l = mid + 1
            
        return list(intersection)

