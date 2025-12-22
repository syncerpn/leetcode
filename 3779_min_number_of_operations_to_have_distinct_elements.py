# easy
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        d = set()
        for i in range(n-1, -1, -1):
            if nums[i] in d:
                return i // 3 + 1
            d.add(nums[i])
        return 0