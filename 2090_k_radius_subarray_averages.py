# easy
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        p = 0
        n = len(nums)
        ans = [-1] * n
        for i, a in enumerate(nums):
            p += a
            if i >= 2 * k + 1:
                p -= nums[i-2*k-1]
            if i >= 2*k:
                ans[i-k] = p // (2*k+1)
        return ans