# simply counting
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        for n in arr:
            if n not in d:
                d[n] = 0
            d[n] += 1
        m = -1
        for n in d:
            if n == d[n]:
                m = max(n, m)
        return m