# kadane's algorithm
# max pos so far and min neg so far kind of like that
# also, maybe reading previous daily challenges is helpful: #1524
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n, p = 0, 0
        ans = 0
        for a in nums:
            p = max(p+a, 0)
            n = min(n+a, 0)
            ans = max(ans, max(p, -n))
        return ans

# another brilliant way to think of this
# is thinking about how we can quicly compute a subarray sum
# via prefix sum
# so, the max subarray sum is simply the max prefix minus the min prefix sum
# because it is absolute sum
# note: initial = 0 is necessary for the case of all positive or all negative
# (so that the best subarray starts at 0)
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        p = list(accumulate(nums, initial=0))
        return max(p) - min(p)