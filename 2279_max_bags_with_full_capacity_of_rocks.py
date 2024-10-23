# greedily fill the bags which are nearly full
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        crs = sorted([c - r for c, r in zip(capacity, rocks)])
        ans = 0
        for cr in crs:
            if cr <= additionalRocks:
                ans += 1
            additionalRocks -= cr
            if additionalRocks <= 0:
                break
        return ans