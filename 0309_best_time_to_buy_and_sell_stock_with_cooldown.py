# need to track the max profit cooldown valid
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        CONSTRAINTS_MIN = -1000
        tk0_cooldown = 0
        tk0 = 0
        tk1 = CONSTRAINTS_MIN
        for p in prices:
            tk0_before_update = tk0
            tk0 = max(tk0, tk1 + p)
            tk1 = max(tk1, tk0_cooldown - p)
            tk0_cooldown = tk0_before_update
        return tk0