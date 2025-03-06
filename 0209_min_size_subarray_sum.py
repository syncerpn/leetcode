# prefix sum + sliding window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p = list(accumulate(nums, initial=0))
        l, r, n = 0, 1, len(nums)
        ans = n + 1
        while r <= n:
            if p[r] - p[l] < target:
                r += 1
            else:
                ans = min(ans, r - l)
                l += 1
        
        return ans % (n + 1)

# or just no prefix sum needed
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, s, n = 0, 0, 0, len(nums)
        ans = n + 1
        for r in range(n):
            s += nums[r]
            while s >= target:
                if r - l + 1 < ans:
                    ans = r - l + 1
                s -= nums[l]
                l += 1

        return ans % (n + 1)

# since it asks for a O(nlogn) solution
# how about binary search
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p = list(accumulate(nums, initial=0))
        n = len(nums)
        ans = n + 1
        for r in range(1, n+1):
            l = bisect.bisect_right(p, p[r] - target)
            if l > 0:
                ans = min(ans, r - l + 1)
        
        return ans % (n + 1)