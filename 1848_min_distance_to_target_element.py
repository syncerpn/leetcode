# just check from start expanding in two directions until we reach one that equals target
# then early stop there
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        i = 0
        while start - i >= 0 or start + i < len(nums):
            if start - i >= 0 and nums[start - i] == target:
                return i
            if start + i < len(nums) and nums[start + i] == target:
                return i
            i += 1
        
        return -1