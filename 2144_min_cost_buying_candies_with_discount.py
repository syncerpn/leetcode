# greedily buy the two most expensive ones in the remaining to get one next expensive for free
# until the end
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        n = len(cost)
        r = 0
        for i in range(n):
            if i % 3 != n % 3:
                r += cost[i]
        return r