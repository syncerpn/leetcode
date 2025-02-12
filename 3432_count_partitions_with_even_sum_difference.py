# just need to check whether the sum of all nums is even or odd
# no need prefix sum or else
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return 0 if sum(nums) % 2 else len(nums) - 1