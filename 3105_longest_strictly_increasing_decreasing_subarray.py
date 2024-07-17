# sounds easy at first
# but strictly inc/dec conditions make it much harder
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        d = nums[1] - nums[0]
        c = 1 + (d != 0)
        c_max = c

        for a, b in pairwise(nums[1:]):
            if (b - a > 0 and d > 0) or (b - a < 0 and d < 0):
                c += 1
            else:
                c_max = max(c_max, c)
                d = b - a
                c = 1 + (d != 0)
        
        c_max = max(c_max, c)
        return c_max

# beautifully clean solution down there
# copied from others
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        incr, decr, ans = 1, 1,1
        prev = nums.pop(0)

        for num in nums:

            incr = incr * (num > prev) + 1
            decr = decr * (num < prev) + 1
            prev = num

            ans = max(ans, incr, decr)
            
        return ans