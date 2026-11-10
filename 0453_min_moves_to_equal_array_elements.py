# solved beautifully by thinking about the equivalent problem
# where instead of add one to n - 1 elements
# we subtract one from 1 element
# so we want to make all array elements equal to the min element
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        n, mi = len(nums), min(nums)
        ans = 0
        for a in nums:
            ans += a - mi
        return ans