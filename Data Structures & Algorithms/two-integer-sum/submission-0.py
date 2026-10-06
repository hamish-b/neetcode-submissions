class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        minus_nums = [target - num for num in nums]
        hash_table = [[] for _ in range(N)]

        def compare_pairwise(array):
            for i in range(len(array)):
                for j in range(i+1, len(array)):
                    if array[i][0] == array[j][0]:
                        return array[i][1], array[j][1]

        def add(hash_table, nums):
            for i in range(N):
                hash_table[nums[i] % N].append((nums[i], i))
            return hash_table

        add(hash_table, nums)
        add(hash_table, minus_nums)

        for layer in hash_table:
            if compare_pairwise(layer) != None:
                i, j = compare_pairwise(layer)
                ans = [i, j]
                ans.sort()
                return ans