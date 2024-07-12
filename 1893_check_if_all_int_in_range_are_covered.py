# line sweep O(m+n)
# efficient, more than assigning everything element of v within each range
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        v = [0] * 52
        for s, e in ranges:
            v[s] += 1
            v[e+1] -= 1
        
        overlaps = 0
        for i in range(1, right+1):
            overlaps += v[i]
            if i >= left and overlaps == 0:
                return False
        
        return True