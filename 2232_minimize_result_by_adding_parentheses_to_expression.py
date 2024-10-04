# brute-force as well
class Solution:
    def minimizeResult(self, expression: str) -> str:
        n, m = expression.split("+")
        ans_v = int(n) + int(m)
        ans = (0, len(m))
        for i in range(len(n)):
            nh = int(n[:i]) if i > 0 else 1
            nt = int(n[i:])
            for j in range(1,len(m)+1):
                mh = int(m[:j])
                mt = int(m[j:]) if j < len(m) else 1
                v = nh * (nt + mh) * mt
                if ans_v > v:
                    ans_v = v
                    ans = (i, j)
        i, j = ans
        n = n[:i] + "(" + n[i:]
        m = m[:j] + ")" + m[j:]
        return n + "+" + m