class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # first we want to find the longest palindrome given at a fixed point in the string
        def lP_fixed(s, base_index, L):

            n = len(s)
            
            if L == 1:
                i = base_index
                score = 1
                
                for k in range(1, n):
                    if i-k <0 or i+k > n-1:
                        break
                    else:
                        if s[i-k] == s[i+k]:
                            score += 2
                        else:
                            break
            else:
                i, j = base_index # i = j - 1
                if s[i] == s[j]:
                    score = 2
                    for k in range(1, n):
                        if i-k <0 or j+k > n-1:
                            break
                        else:
                            if s[i-k] == s[j+k]:
                                score += 2
                            else:
                                break
                else:
                    return 0
            return score

        # now we want to run it through every possible starting point
        # this includes each element of the string, as well as all pairs of elements adjacent to each other
        max_score = 0
        max_palindrome = ""
        for a in range(len(s)):
            iter_score = lP_fixed(s, a, 1)
            if iter_score > max_score:
                max_score = iter_score
                max_palindrome = s[a - iter_score // 2: a + 1 + iter_score // 2] 

        for a in range(len(s) - 1):
            iter_score = lP_fixed(s, (a, a+1), 2)
            if iter_score > max_score:
                max_score = iter_score
                max_palindrome = s[a - iter_score // 2 + 1: a + 1+ iter_score // 2]
        return max_palindrome 