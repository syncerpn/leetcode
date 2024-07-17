# hash table for remembering indices
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        r = 0
        d = {}
        for i, c in enumerate(s):
            d[c] = i
        for i, c in enumerate(t):
            r += abs(d[c] - i)
        return r