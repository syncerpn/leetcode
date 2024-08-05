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