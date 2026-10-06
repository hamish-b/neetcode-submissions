class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        N = len(nums)

        best_0 = nums[0]

        list_of_bests = [best_0]
        best_so_far = best_0

        for i in range(1, N):
            prev_best = list_of_bests[i-1]
            if prev_best > 0:
                current = prev_best + nums[i]
                
            else:
                current = nums[i]

            list_of_bests.append(current)

            if current > best_so_far:
                best_so_far = current
        return best_so_far
# this above solution assumes we wrap around (which is actually harder)
        