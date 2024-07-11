# fairly simple
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = 0
        n_next = nums[0] + 1
        for i in range(1, len(nums)):
            if nums[i] < n_next:
                c += n_next - nums[i]
                n_next += 1
            else:
                n_next = nums[i] + 1
        return c