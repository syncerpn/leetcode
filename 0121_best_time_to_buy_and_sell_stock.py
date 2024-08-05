# kadane's algorithm
# keep track of minimum stock price while considering on-going profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]
        profit = 0
        for p in prices:
            if p < cur_min:
                cur_min = p
            elif p - cur_min > profit:
                profit = p - cur_min
        
        return profit

# general solution
# this is a scalable dp solution
# may not be optimal to a specific case, but it is still good
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        CONSTRAINTS_MIN = - 10 ** 4 - 1
        tk0 = 0
        tk1 = CONSTRAINTS_MIN
        for p in prices:
            tk0, tk1 = max(tk0, tk1 + p), max(tk1, -p)
        return tk0