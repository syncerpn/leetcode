# just calculate it
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        e = sum(nums)
        d = 0
        for n in nums:
            for c in str(n):
                d += int(c)
        
        return abs(d - e)