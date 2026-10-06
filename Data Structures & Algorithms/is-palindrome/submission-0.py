class Solution:
    def isPalindrome(self, s: str) -> bool:
        # want to implement two pointer technique

        s_new = ''.join([char for char in s if char.isalnum()])
        N = len(s_new)
        left, right = 0, N - 1
        mid = N // 2

        # clearly this problem has symmetry, if i = j for the first N//2 chars
        # we are done

        for i in range(N // 2):
            if s_new[i].lower() != s_new[right - i].lower():
                return False
        return True