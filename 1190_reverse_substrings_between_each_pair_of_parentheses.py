# not that difficult though
# stack, obviously
class Solution:
    def reverseParentheses(self, s: str) -> str:
        r = []
        for c in s:
            if c == ")":
                t = ""
                while r[-1] != "(":
                    t += r.pop()[::-1]
                
                r.pop()
                r.append(t)
            else:
                r.append(c)
        
        return "".join(r)