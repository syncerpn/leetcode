# sort and binary search, finding lower and upper of nums[j] for each nums[i]
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n-1):
            l = bisect.bisect_left(nums, lower-nums[i], lo=i+1)
            r = bisect.bisect_right(nums, upper-nums[i], lo=i+1)
            ans += r - l
        return ans