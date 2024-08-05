# easy to verify, thus it should be binary search
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def valid(k):
            t = 0
            d = days
            for w in weights:
                if t + w > k:
                    d -= 1
                    if d == 0:
                        return False
                    t = 0
                t += w
            return True

        l = max(weights)
        r = sum(weights)
        while l <= r:
            m = (l + r) // 2
            if valid(m):
                r = m - 1
            else:
                l = m + 1
        return r + 1