# greedy
# remove all same-color adjacent balloons except the one with highest time
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n, ans = len(colors), 0
        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                ans += min(neededTime[i], neededTime[i - 1])
                neededTime[i] = max(neededTime[i], neededTime[i - 1])
        return ans
        