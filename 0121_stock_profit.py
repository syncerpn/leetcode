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