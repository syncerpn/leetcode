# monostack + binary search for an O(nlogn) solution
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans = 0
        s = []
        for i, n in enumerate(nums):
            if not s or s[-1][0] < -n:
                s.append((-n, -i))
            else:
                j = bisect_right(s, (-n, -i))
                ans = max(ans, i + s[j][1])
        return ans

# improved into two-pass O(n)
# keep a monostack as before
# then the second pass going backward, trying to empty the stack
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans = 0
        s = []
        n = len(nums)
        for i in range(n):
            if not s or nums[s[-1]] > nums[i]:
                s.append(i)
        for i in range(n-1,-1,-1):
            while s and nums[s[-1]] <= nums[i]:
                ans = max(ans, i-s.pop())

        return ans