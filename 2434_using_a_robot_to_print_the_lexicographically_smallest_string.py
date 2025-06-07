# try to pick the smallest char while iterating s
# if not the smallest, save it to t
# pop from t when cannot find any char smaller than top of t stack
class Solution:
    def robotWithString(self, s: str) -> str:
        A = "abcdefghijklmnopqrstuvwxyz"
        d = Counter(s)
        def min_char(d):
            for c in A:
                if d[c] > 0:
                    return c
            return "a"
        
        t = []
        p = []
        for c in s:
            t.append(c)
            d[c] -= 1
            while t and t[-1] <= min_char(d):
                p.append(t.pop())
        
        while t:
            p.append(t.pop())
        
        return "".join(p)