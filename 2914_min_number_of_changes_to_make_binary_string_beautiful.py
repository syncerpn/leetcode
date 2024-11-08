# simply check any pair of chars if they have the same character ("00" or "11")
class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0
        for i in range(0,len(s),2):
            if s[i] != s[i+1]:
                ans += 1
        return ans