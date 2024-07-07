# just find the two largest nums
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p = min(nums[0], nums[1])
        c = max(nums[0], nums[1])
        for n in nums[2:]:
            if n >= c:
                p, c = c, n
            elif n >= p:
                p = n
        return (p-1) * (c-1)