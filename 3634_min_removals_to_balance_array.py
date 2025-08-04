# two-pointer
# greedy did not work
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        r = 0
        ans = n - 1
        for i, a in enumerate(nums):
            while r < n and a * k >= nums[r]:
                r += 1
            ans = min(ans, i + n - r)
        return ans