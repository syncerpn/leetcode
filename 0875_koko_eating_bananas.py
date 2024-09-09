# binary search
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_valid(k):
            t = 0
            for p in piles:
                t += p // k + (p % k > 0)
                if t > h:
                    return False
            return True
        
        l = 1
        r = max(piles)
        while l < r:
            m = (l + r) // 2
            if is_valid(m):
                r = m
            else:
                l = m + 1
        return r