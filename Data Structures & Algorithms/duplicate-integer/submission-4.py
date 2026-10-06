class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    
        N = len(nums)
        hash_table = [[] for _ in range(N)]

        def add(hash_table, nums):
            for num in nums:
                hash_table[num % N].append(num)
            return hash_table

        def check_dupe_pair(array):
            for i in range(len(array)):
                for j in range(i+1, len(array)):
                    if array[i] == array[j]:
                        return True
            return False            

        add(hash_table, nums)

        for layer in hash_table:
            if len(layer) > 1:
                if check_dupe_pair(layer) == True:
                    return True
        
        return False

        
