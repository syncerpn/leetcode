# binary search obviously
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def is_valid(m):
            return sum(c // m for c in candies) >= k
        
        l, r = 1, max(candies)
        ans = 0
        while l <= r:
            m = (l + r) // 2
            if is_valid(m):
                ans = m
                l = m + 1
            else:
                r = m - 1
        
        return ans