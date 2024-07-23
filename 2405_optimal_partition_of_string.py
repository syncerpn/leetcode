# use set
class Solution:
    def partitionString(self, s: str) -> int:
        r = set()
        ans = 1
        for c in s:
            if c in r:
                ans += 1
                r = set()
            r.add(c)
        return ans