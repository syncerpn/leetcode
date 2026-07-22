# easy
class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        ans = -inf
        m = -inf
        for j, a in enumerate(nums):
            if j >= k:
                ans = max(ans, a + nums[j-k])
            m = max(m, a)
            nums[j] = m
        return ans

# better runtime
class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n < k + 1:
            return -1
        ans = -inf
        m = -inf
        for i in range(n-k):
            m = max(m, nums[i])
            ans = max(ans, m + nums[i+k])
        return ans