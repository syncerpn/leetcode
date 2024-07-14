# lol, why need actual sorting here
# just count num of appearance of target and num of those smaller than target
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lt = 0
        eq = 0
        for n in nums:
            if n < target:
                lt += 1
            elif n == target:
                eq += 1
        
        return list(range(lt, lt+eq))