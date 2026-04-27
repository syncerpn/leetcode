# fairly easy with math
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f, s = 0, 0
        for i, a in enumerate(nums):
            f += i * a
            s += a
        
        ans = f
        n = len(nums)
        for i in range(n-1, 0, -1):
            f = f - (n - 1) * nums[i] + s - nums[i]
            ans = max(ans, f)
        return ans
