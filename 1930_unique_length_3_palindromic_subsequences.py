# one way, kinda one-pass, but it is quite slow
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        d = {}
        p = set()
        for c in s:
            for k in d:
                if k == c:
                    p |= d[k]
                d[k].add(k + c)
            if c not in d:
                d[c] = set()
        return len(p)

# likely the same but with lib
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for c in string.ascii_lowercase:
            i, j = s.find(c), s.rfind(c)
            if i > -1:
                res += len(set(s[i + 1: j]))
        return res