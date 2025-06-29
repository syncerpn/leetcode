# easy
class Solution:
    def partitionString(self, s: str) -> List[str]:
        v = set()
        ans = []
        c = ""
        for a in s:
            c += a
            if c not in v:
                v.add(c)
                ans.append(c)
                c = ""
        return ans