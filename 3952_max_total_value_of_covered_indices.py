# greedy
class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        i, j = 0, -1
        ans = 0
        m = inf
        for i, a in enumerate(nums):
            ans += a
            if s[i] == "1":
                m = min(m, a)
            else:
                if j >= 0:
                    ans -= m
                j = i
                m = a
        
        return ans if j == -1 else ans - m