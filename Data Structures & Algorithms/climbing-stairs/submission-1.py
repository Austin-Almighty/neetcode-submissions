class Solution:

    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        cache = [1, 1]
        i = 1
        while i < n:
            cache[0], cache[1] = cache[1], cache[0] + cache[1]
            i += 1

        return cache[1]
        