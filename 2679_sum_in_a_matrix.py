# matrix manip
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        nums = [sorted(row) for row in nums]
        nums = list(zip(*nums))
        return sum(max(row) for row in nums)