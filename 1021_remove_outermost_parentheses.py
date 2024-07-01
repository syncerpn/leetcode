class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        k = 0
        r = ""
        for c in s:
            if c == "(":
                if k > 0:
                    r += c
                k += 1
            elif c == ")":
                k -= 1
                if k > 0:
                    r += c
        return r