# compare new number with max
# easy
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        r = [False] * len(candies)
        for i, n in enumerate(candies):
            if n + extraCandies >= m:
                r[i] = True
        return r