# if you dont have to choose k distinct subarrays,
# just choose one k times, lol
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return k * (max(nums) - min(nums))