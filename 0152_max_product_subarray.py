# dp solution
# tracking both product max and min
# min should be negative with high absolute value
# it can turn into max anytime it multiplies with another negative
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        cmin, cmax = 1, 1
        for n in nums:
            cmin, cmax = min(cmin * n, cmax * n, n), max(cmin * n, cmax * n, n)
            ans = max(ans, cmax)
        return ans

# lee's solution using prefix and suffix product
# a quote explains the solution:
# This algorithms is based on one conclusion:
# the max product must either start with 0 or end with n-1.
# That is, if A[i..j] is the subarray of max product,
# then i==0 or j==n-1 must be true.
# With this claim, we can simply start cumulative product from both ends
# and find the maximum product from both arrays.
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        smun = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            smun[i] *= smun[i-1] or 1
        return max(nums + smun)