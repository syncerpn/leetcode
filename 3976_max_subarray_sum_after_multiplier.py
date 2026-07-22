# nice prob
# at first, it looks just like kadane
# but some edge cases make me realize it has more states
# so just dp
# dp0: the subarray has not undergone any operation
# dpb: the subarray is currently being multiplied by k
# dpc: the subarray is currently being divided by k
# dp1: the subarray has finished its operations and returned to standard elements
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        ans = dp0 = dpb = dpc = dp1 = -inf
        for a in nums:
            b, c = a * k, int(a / k)
            dp1 = max(dp1 + a, dpb + a, dpc + a)
            dpb = max(dp0 + b, dpb + b, b)
            dpc = max(dp0 + c, dpc + c, c)
            dp0 = max(dp0 + a, a)
            ans = max(ans, dp0, dpb, dpc, dp1)
        return ans