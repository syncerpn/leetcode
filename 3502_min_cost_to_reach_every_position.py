# easy
class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        m = cost[0]
        ans = []
        for a in cost:
            m = min(m, a)
            ans.append(m)
        return ans
