# easy
class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        p = nums[0]
        l = 1
        n = len(nums)
        ans = 0
        for i in range(1, n):
            a = nums[i]
            if a != p:
                l += 1
            else:
                ans += l * (l + 1) // 2
                l = 1
            p = a
        ans += l * (l + 1) // 2
        return ans