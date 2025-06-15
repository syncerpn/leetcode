# lee's solution
# keep track of
# res[j]: best total profit after completing j transactions
# bought[j]: best profit if we just bought and are waiting to sell
# sold[j]: best profit if we just sold and are waiting to buy back
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        bought = [-inf] * k
        res = [0] * (k + 1)
        sold = [0] * k
        for a in prices:
            for j in range(k, 0, -1):
                res[j] = max(res[j], bought[j - 1] + a, sold[j - 1] - a)
                bought[j - 1] = max(bought[j - 1], res[j - 1] - a)
                sold[j - 1] = max(sold[j - 1], res[j - 1] + a)
        return max(res)
        