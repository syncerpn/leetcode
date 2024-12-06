# greedy
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        ans = 0
        for i in range(1, n+1):
            if i in banned:
                continue
            if maxSum - i < 0:
                break
            maxSum -= i
            ans += 1
        return ans