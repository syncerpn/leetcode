# easy
class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        d = Counter(list(s))
        m = max(d.values())
        n = len(s)
        v = set()
        ans = ""
        for i in range(n):
            c = s[~i]
            if d[c] == m and c not in v:
                v.add(c)
                ans += c
        return ans[::-1]