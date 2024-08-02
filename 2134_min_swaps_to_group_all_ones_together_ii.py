# the target should have all ones together
# we count the number of ones, "s", in the whole array
# then use sliding window of size s to slide the extended array (appended itself at the end)
# every slide shows how many ones already in place
# and number of zeros is the number of swaps needed
# find the min number of swaps
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        s = sum(nums)
        n = len(nums)
        nums += nums
        p = 0
        ans = s
        for i in range(n+s):
            p += nums[i]
            if i >= s:
                p -= nums[i-s]
            if i >= s - 1:
                ans = min(ans, s - p)
        return ans
