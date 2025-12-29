# ask yourself when to use costBoth
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if costBoth <= cost1 + cost2:
            return min(need1, need2) * costBoth + ((need1 - need2) * min(cost1, costBoth) if need1 > need2 else (need2 - need1) * min(cost2, costBoth))
        return need2 * min(costBoth, cost2) + need1 * min(costBoth, cost1)