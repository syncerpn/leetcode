# now with even more general than #0123
# we need 2d dp
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        CONSTRAINTS_MIN = -1000
        t = [[0, CONSTRAINTS_MIN] for _ in range(k+1)]
        for p in prices:
            for j in range(k,0,-1):
                t[j][0] = max(t[j][0], t[j][1] + p)
                t[j][1] = max(t[j][1], t[j-1][0] - p)
        return t[k][0]