# first element is a must
# other than that, just pick the two min out of the remaining
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        s = sorted(nums[1:])
        return nums[0] + s[0] + s[1]