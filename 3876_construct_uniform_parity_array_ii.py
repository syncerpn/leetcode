# easy math
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return min(nums1) % 2 == 1 or all([a % 2 == 0 for a in nums1])