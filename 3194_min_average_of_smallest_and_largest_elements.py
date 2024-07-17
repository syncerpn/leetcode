# sort to choose numbers
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        m = nums[0] + nums[-1]
        n = len(nums)
        for i in range(1, n // 2 + 1):
            m = min(m, nums[i] + nums[n-1-i])
        return m / 2