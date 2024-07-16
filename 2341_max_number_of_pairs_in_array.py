# count, but use boolean for a bit of optimization
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        l = 0
        d = {}
        for n in nums:
            if n not in d:
                d[n] = False
            d[n] = not d[n]
        
        for n in d:
            if d[n]:
                l += 1
        
        return [(len(nums) - l) // 2, l]