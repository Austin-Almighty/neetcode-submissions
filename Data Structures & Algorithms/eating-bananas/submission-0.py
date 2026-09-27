import math
from functools import reduce
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        ans = high

        while high >= low:
            mid = (low + high) // 2
            total = reduce(lambda acc, x: acc + math.ceil(x / mid), piles, 0)
            
            match total:
                case _ if total <= h:
                    ans = mid
                    high = mid - 1
                case _:
                    low = mid + 1
            
        return ans