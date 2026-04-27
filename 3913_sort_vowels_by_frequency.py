# easy
class Solution:
    def sortVowels(self, s: str) -> str:
        V = "aeiou"
        f = {}
        q = {}
        s = list(s)
        for i, c in enumerate(s):
            if c in V:
                if c not in f:
                    f[c] = 0
                    q[c] = i
                f[c] += 1
        S = sorted([(-f[c], q[c], c) for c in f])
        ss = "".join([-a * c for a, _, c in S])
        j = 0
        for i in range(len(s)):
            if s[i] in V:
                s[i] = ss[j]
                j += 1
        return "".join(s)
