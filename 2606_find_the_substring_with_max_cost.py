# prefix sum and max
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        d = {c: i+1 for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        for c, v in zip(chars, vals):
            d[c] = v
        ans = 0
        p = [0]
        q = [0]
        n = len(s)
        for c in s:
            p.append(p[-1] + d[c])
            q.append(q[-1] + d[c])
        
        m = -inf
        for i in range(n, -1, -1):
            m = max(q[i], m)
            q[i] = m
        
        for i in range(n+1):
            ans = max(ans, q[i] - p[i])
        return ans

# could be easier with kadane algorithm
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        d = {c: i+1 for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        for c, v in zip(chars, vals):
            d[c] = v
        
        ans = 0
        p = 0
        for c in s:
            p += d[c]
            if p < 0:
                p = 0
            ans = max(ans, p)
        return ans