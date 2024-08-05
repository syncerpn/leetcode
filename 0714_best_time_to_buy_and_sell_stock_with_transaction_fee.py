# same as #0122, but with fee when sell
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        CONSTRAINTS_MIN = - 5 * 10 ** 4 - 1 - fee
        tk0 = 0
        tk1 = CONSTRAINTS_MIN
        for p in prices:
            tk0, tk1 = max(tk0, tk1 + p), max(tk1, tk0 - p - fee)
        return tk0