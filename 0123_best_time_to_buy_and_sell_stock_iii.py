# more general than #0122
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        CONSTRAINTS_MIN = - 10 ** 4 - 1
        t10 = 0 # max profit having 0 stocks in hand after 1 transaction (finished 1 transtion)
        t11 = CONSTRAINTS_MIN # max profit having 1 stocks in hand after 1 transaction (under 1st transtion yet not finished)
        t20 = 0 # max profit having 0 stocks in hand after 2 transactions (finished 2 transtions)
        t21 = CONSTRAINTS_MIN # max profit having 1 stocks in hand after 2 transactions (under 2nd transtion yet not finished)
        for p in prices:
            t20 = max(t20, t21 + p)
            t21 = max(t21, t10 - p)
            t10 = max(t10, t11 + p)
            t11 = max(t11, -p)
        return t20