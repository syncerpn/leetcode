# brute force edition
# not that a special substring is formed by only a single letter
# that why i failed at first
class Solution:
    def maximumLength(self, s: str) -> int:
        ans = -1
        n = len(s)
        for k in range(1, n+1):
            d = {}
            for i in range(n-k+1):
                w = s[i:i+k]
                if len(set(w)) > 1:
                    continue
                if w not in d:
                    d[w] = 0
                d[w] += 1
                if d[w] == 3:
                    ans = k
                    break
        return ans

# much faster using the characteristics of special strings
class Solution:
    def maximumLength(self, s: str) -> int:
        d = {}
        p = "."
        for c in s:
            if c != p[-1]:
                p = c
            else:
                p += c
            if p not in d:
                d[p] = 0
            d[p] += 1
        
        ans = -1
        for c in d:
            if d[c] >= 3:
                ans = max(ans, len(c))
            elif len(c) >= 3:
                if d[c[:-1]] >= 2:
                    ans = max(ans, len(c)-1)
                else:
                    ans = max(ans, len(c)-2)
            elif len(c) == 2:
                if d[c[:-1]] >= 2:
                    ans = max(ans, len(c)-1)
        return ans