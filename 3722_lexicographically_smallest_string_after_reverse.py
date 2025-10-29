# bruteforce
class Solution:
    def lexSmallest(self, s: str) -> str:
        ans = s
        for i, c in enumerate(s):
            ans = min(ans, s[:i][::-1] + s[i:], s[:i] + s[i:][::-1])
        return ans