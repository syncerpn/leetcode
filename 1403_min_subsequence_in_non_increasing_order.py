# the description is pretty confusing
# yet we can solve it easily with sorting and prefix sum
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        s = sum(nums)
        p = 0
        for i, n in enumerate(nums):
            p += n
            if p > s - p:
                return nums[:i+1]
        return nums