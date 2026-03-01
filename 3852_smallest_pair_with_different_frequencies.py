# easy
class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        d = Counter(nums)
        f = {}
        for a in d:
            v = d[a]
            if v not in f:
                f[v] = a
            f[v] = min(f[v], a)
        s = sorted([f[k] for k in f])
        if len(s) < 2:
            return [-1, -1]
        return [s[0], s[1]]