# see #0121
# in this one, we have accumulated profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        CONSTRAINTS_MIN = - 10 ** 4 - 1
        tk0 = 0
        tk1 = CONSTRAINTS_MIN
        for p in prices:
            tk0, tk1 = max(tk0, tk1 + p), max(tk1, tk0 - p)
        return tk0

# revisit 260506
# could not solve it
# so found a way to make it more intuitive
# for every step, we may buy the stock if it immediately generate profit in the next step
# this is optimal, because if we buy a stock that does not generate profit in the next step
# meaning that that next step, the price is smaller
# so it is always better to not buy this one, and buy only the next one to get a higher difference/profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for a, b in pairwise(prices):
            ans += max(b-a, 0)
        return ans