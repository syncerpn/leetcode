# sliding window
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        d = sum(s * p for p, s in zip(prices, strategy))
        rr = sum(prices[i] * strategy[i] for i in range(k))
        ss = sum(prices[i] for i in range(k//2, k))
        pp = max(0, ss - rr)
        for i in range(n-k):
            rr = rr - prices[i] * strategy[i] + prices[i+k] * strategy[i+k]
            ss = ss - prices[i+k//2] + prices[i+k]
            pp = max(pp, ss - rr)

        return d + pp