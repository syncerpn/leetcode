# greedy
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        i, j, n = 0, 1, len(nums)
        while j < n:
            if nums[j] > nums[i]:
                ans += 1
                i += 1
            j += 1
        return ans