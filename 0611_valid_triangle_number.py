# pair-wise
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n-2):
            a = nums[i]
            for j in range(i+1, n-1):
                b = nums[j]
                k = bisect.bisect_left(nums, a + b)
                ans += max(0, k - j - 1)
        return ans