# solved with dp
# we just need to keep track of the cost to reach two prev steps
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev_two = 0
        prev_one = 0
        curr = 0
        for i in range(2, len(cost)+1):
            curr = min(prev_two + cost[i-2], prev_one + cost[i-1])
            prev_two, prev_one = prev_one, curr
        return curr

# compact solution
# we either climb from prev 2-step or 1-step
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp_2 = cost[0]
        dp_1 = cost[1]
        for c in cost[2:]:
            dp_2, dp_1 = dp_1, min(dp_2 + c, dp_1 + c)
        return min(dp_2, dp_1)