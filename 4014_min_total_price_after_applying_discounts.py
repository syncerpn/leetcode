# easy
class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        m = len(discounts)
        discounts.sort(reverse=True)
        prices.sort(reverse=True)
        ans = 0
        
        for i, p in enumerate(prices):
            d = 0
            if i < m:
                d = discounts[i]
            ans += p * (100 - d)
        return ans / 100