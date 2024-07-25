# pure stack
# should be easy instead of medium
class Solution:
    def removeStars(self, s: str) -> str:
        r = []
        for c in s:
            if c == "*":
                r.pop()
            else:
                r.append(c)
        return "".join(r)