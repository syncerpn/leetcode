# see this a lot
# sliding window and compressing
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        def is_valid(d):
            for c in d:
                if d[c] == 0:
                    return False
            return True
        d = {c: 0 for c in "abc"}
        n = len(s)
        ans = 0
        l = 0
        for r in range(n):
            d[s[r]] += 1
            j = l
            while is_valid(d):
                d[s[j]] -= 1
                j += 1
            ans += (n - r) * (j - l)
            l = j
        return ans