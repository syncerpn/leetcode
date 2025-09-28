# simple dp
# how about cheating mem optimization a bit
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        costs[0] += 1
        if n >= 2:
            costs[1] += min(costs[0] + 1, 4)
        if n >= 3:
            costs[2] += min(costs[1] + 1, costs[0] + 4, 9)
        for i in range(3, n):
            costs[i] += min(costs[i-1] + 1, costs[i-2] + 4, costs[i-3] + 9)
        return costs[n-1]