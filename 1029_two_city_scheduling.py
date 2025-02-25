# greedy sorting diff
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        d = sorted([i for i in range(2*n)], key=lambda i: costs[i][0]-costs[i][1])
        ans = 0
        for j, i in enumerate(d):
            if j >= n:
                ans += costs[i][1]
            else:
                ans += costs[i][0]
        return ans