# simple binary search
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n
        
        while l + 1 < r:
            m = (r + l) // 2
            if nums[0] < nums[m]:
                l = m
            else:
                r = m
        return nums[r % n]