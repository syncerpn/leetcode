# same as #1653
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = 0
        ones = 0
        for c in s:
            if c == "0":
                ans = min(ones, ans+1)
            else:
                ones += 1
        return ans