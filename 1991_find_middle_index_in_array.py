# prefix sum obviously
# if sum of nums is counted as one pass, then we need two pass
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        l = 0
        for i in range(n):
            if s - nums[i] == 2 * l:
                return i
            l += nums[i]
        
        return -1