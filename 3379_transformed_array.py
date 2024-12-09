# easy
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        for i, a in enumerate(nums):
            j = (i + a) % n
            ans[i] = nums[j]
        return ans