# O(n) space
# may solve with O(1) space using two-pointer
class Solution:
    def reverseByType(self, s: str) -> str:
        A = "abcdefghijklmnopqrstuvwxyz"
        s = list(s)
        p, q = [], []
        for i, c in enumerate(s):
            if c in A:
                p.append(i)
            else:
                q.append(i)
        
        for i in range(len(p) // 2):
            s[p[i]], s[p[~i]] = s[p[~i]], s[p[i]]
            
        for i in range(len(q) // 2):
            s[q[i]], s[q[~i]] = s[q[~i]], s[q[i]]
        
        return "".join(s)