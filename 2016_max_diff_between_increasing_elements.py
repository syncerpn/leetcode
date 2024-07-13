# just keep track of decreasing elements for diff calculation
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        p = nums[0]
        d = -1
        for n in nums[1:]:
            if n > p:
                d = max(d, n - p)
            else:
                p = n
        return d
