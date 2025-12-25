#easy
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        ans = 0
        for i in range(k):
            ans += max(happiness.pop() - i, 0)
        return ans