# stack, obviously
class Solution:
    def removeDuplicates(self, s: str) -> str:
        r = []
        for c in s:
            if r and r[-1] == c:
                r.pop()
            else:
                r.append(c)
        
        return "".join(r)
