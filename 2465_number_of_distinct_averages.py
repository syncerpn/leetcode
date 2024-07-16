# average, but number of elements is fixed at 2
# so just calculate sum
# sort first, then form a set
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        s = set([nums[i] + nums[n-1-i] for i in range(n//2)])
        return len(s)