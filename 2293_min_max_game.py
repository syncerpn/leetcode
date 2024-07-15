# simulate it
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        def op(i):
            return min(nums[2*i:2*i+2]) if i % 2 == 0 else max(nums[2*i:2*i+2])

        while len(nums) != 1:
            n = len(nums)
            nums = [op(i) for i in range(n // 2)]
        return nums[0]