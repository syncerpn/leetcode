# easy
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {}
        for i, a in enumerate(nums):
            d[a] = i
        for a, b in operations:
            d[b] = d[a]
            del d[a]
        for a in d:
            nums[d[a]] = a
        return nums