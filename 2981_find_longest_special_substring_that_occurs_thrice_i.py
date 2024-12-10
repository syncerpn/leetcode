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