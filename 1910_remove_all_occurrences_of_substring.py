# trivial solution
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        part = list(part)
        r = []
        p = len(part)
        for c in s:
            r.append(c)
            if len(r) >= len(part) and r[-p:] == part:
                for _ in range(p):
                    r.pop()
        return "".join(r)

# and kmp
# it has been a long time yet i havent been able to fully understand this one
# copied from others
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        lps = [0]
        k = 0 
        for i in range(1, len(part)): 
            while k and part[k] != part[i]: k = lps[k-1]
            if part[k] == part[i]: k += 1
            lps.append(k)
        
        stack = [("", 0)]
        for ch in s: 
            k = stack[-1][1]
            while k and part[k] != ch: k = lps[k-1]
            if part[k] == ch: k += 1
            stack.append((ch, k))
            if k == len(part): 
                for _ in range(len(part)): stack.pop()
        return "".join(x for x, _ in stack)