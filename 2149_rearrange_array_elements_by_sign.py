# O(n) space
# O(1) not that rewarding yet too complicated
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = 0
        n = 1
        ans = [0] * len(nums)
        for k in nums:
            if k > 0:
                ans[p] = k
                p += 2
            if k < 0:
                ans[n] = k
                n += 2
        return ans