# pairing to eliminate as many small numbers as possible
# we can do so by sorting and pairing from smallest to the largest
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[0::2])