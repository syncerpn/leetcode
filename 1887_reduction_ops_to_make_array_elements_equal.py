# simple hash counting
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
        
        r = 0
        for i, k in enumerate(sorted(d.keys())):
            r += i * d[k]
        return r