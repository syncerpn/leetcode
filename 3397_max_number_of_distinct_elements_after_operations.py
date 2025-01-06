# sort and greedy
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        m = -float("inf")
        for i in range(len(nums)):
            if nums[i] - k > m:
                m = nums[i] - k
                nums[i] = m
            else:
                m = nums[i] + min(k, m + 1 - nums[i])
                nums[i] = m
        return len(set(nums))
