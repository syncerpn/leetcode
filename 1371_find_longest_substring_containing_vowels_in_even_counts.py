# did not think of prefix sum at first
# but then it was just beautiful
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        d = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}
        p = {0: -1}
        v = 0
        ans = 0
        for i, c in enumerate(s):
            if c in d:
                v ^= d[c]
            if v not in p:
                p[v] = i
            ans = max(ans, i - p[v])
        return ans