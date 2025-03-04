# fairly simple
# yet need to read the desc carefully
# that a number is almost missing if it appears in exactly one subarray
# so it might appear twice in the same subarray but still valid, lol
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return max(nums)
        
        d = Counter(nums)
        if k == 1:
            return max([-1] + [i for i in d if d[i] == 1])
        return max([-1] + [i for i in [nums[0], nums[-1]] if d[i] == 1])