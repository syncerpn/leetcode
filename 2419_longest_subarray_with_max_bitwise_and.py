# max bitwise of a subarray is actually max of value of the array
# so just need to find the longest subarray of only the max value
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m, l, ans = 0, 0, 0
        for n in nums:
            if n > m:
                m, l, ans = n, 1, 1
            elif n == m:
                l += 1
                ans = max(l, ans)
            else:
                l = 0
        return ans