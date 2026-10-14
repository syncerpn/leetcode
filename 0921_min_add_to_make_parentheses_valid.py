# parentheses and stack are best friend
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        r = 0
        p = []
        for c in s:
            if c == ")":
                if not p:
                    r += 1
                else:
                    p.pop()
            else:
                p.append(c)
        
        r += len(p)
        return r

# why even need stack
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        r = 0
        p = 0
        for c in s:
            if c == ")":
                if p:
                    p -= 1
                else:
                    r += 1
            else:
                p += 1
        return r + p