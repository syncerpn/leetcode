# the way we count the subarrays without duplicates is just simply awesome
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        maxi, mini = -1, -1
        l = 0
        for r, a in enumerate(nums):
            if a < minK or a > maxK:
                l = r + 1
                continue
            if a == maxK:
                maxi = r
            if a == minK:
                mini = r
            ans += max((min(maxi, mini) - l + 1), 0)
        return ans