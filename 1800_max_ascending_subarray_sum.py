# again, tracking ascending subarray and calculate sum
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        s_max = nums[0]
        s = nums[0]
        for a, b in pairwise(nums):
            if a < b:
                s += b
            else:
                s = b
            
            s_max = max(s, s_max)
            
        return s_max