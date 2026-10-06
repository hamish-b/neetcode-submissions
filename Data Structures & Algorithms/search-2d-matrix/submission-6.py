class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # we first want to find the right row using binary search, and then find the number in that row using binary search

        k = len(matrix) # matrix is k x n
        n = len(matrix[0])

        l, r = 0, k - 1

        # binary search to find column

        while l<=r:
            
            m = (l+r) // 2

            if m == k-1:
                break
            if matrix[m][0] <= target < matrix[m+1][0]: # condition for column to be correct
                break
            elif target >= matrix[m][0]:
                l = m + 1
            else:
                r = m - 1

        row = m
        l, r = 0, n-1

        while l <= r:
            m = (l+r) // 2

            if target == matrix[row][m]:
                break
            elif target > matrix[row][m]:
                l = m + 1
            else:
                r = m - 1
        print(row, m)
        return matrix[row][m] == target