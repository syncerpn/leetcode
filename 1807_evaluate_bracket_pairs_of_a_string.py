# fairly easy
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        ans = ""
        d = {k: v for k, v in knowledge}
        b = False
        k = ""
        for c in s:
            if c == "(":
                b = True
            elif c == ")":
                if k in d:
                    ans += d[k]
                else:
                    ans += "?"
                b = False
                k = ""
            elif not b:
                ans += c
            else:
                k += c
        return ans
                