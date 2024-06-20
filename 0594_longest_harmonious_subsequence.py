# counting is probably the way
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
        r = 0
        for k in d:
            if k + 1 not in d:
                continue
            t = d[k] + d[k+1]
            if r < t:
                r = t
        
        return r
