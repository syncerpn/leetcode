# use pure math
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = 0
        for i, n in enumerate(nums):
            x ^= i ^ n
        return x ^ (i+1)

# or bit manip
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) * (len(nums)+1) // 2 - sum(nums)