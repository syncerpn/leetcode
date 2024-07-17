# practice sliding window
# good problem
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        i, j = 0, 0
        d = {}
        l_max = 0
        for j, c in enumerate(s):
            if c not in d:
                d[c] = 0
            d[c] += 1
            while d[c] > 2:
                d[s[i]] -= 1
                i += 1
            l_max = max(l_max, j - i + 1)
        return l_max