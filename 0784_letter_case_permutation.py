# make it bitmask
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        p = []
        r = ""
        for i, c in enumerate(s):
            r += c
            if c.isalpha():
                p.append(r)
                r = ""
        if not p:
            return [s]
        p[-1] += r
        n = len(p)
        ans = []
        for i in range(1 << n):
            ans.append("".join([q.upper() if (i >> j) & 1 else q.lower() for j, q in enumerate(p)]))
        return ans