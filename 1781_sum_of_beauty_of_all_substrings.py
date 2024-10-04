# none better than brute force
# better learn to not overthinking
class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0 
        for i in range(len(s)):
            d = [0] * 26
            for j in range(i, len(s)):
                d[ord(s[j]) - 97] += 1
                ans += max(d) - min(c for c in d if c)
        return ans