class Solution:
    def climbStairs(self, n: int) -> int:
        
        # for n = 1 can climb it one way
        # for n = 2 can climb it two ways
        # for n = 3 (s(2) + s(1) ways) since we can choose to either step once or   step twice initially
        # Hence s(n) = s(n-1) + s(n-2) with s(1) = 1, s(2)
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        current = 2
        prev = 1

        for i in range(n-2):
            new = current + prev
            prev = current
            current = new
        
        return new