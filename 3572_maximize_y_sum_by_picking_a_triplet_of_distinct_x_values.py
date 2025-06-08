# fairly easy
class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        d = {}
        for a, b in zip(x, y):
            if a not in d:
                d[a] = b
            else:
                d[a] = max(d[a], b)
        
        if len(d) < 3:
            return -1
        
        s = sorted(d[a] for a in d)
        return sum(s[-3:])