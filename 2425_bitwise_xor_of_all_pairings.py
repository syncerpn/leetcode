# easy
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        return (reduce(lambda x, y: x ^ y, nums1) if len(nums2) % 2 else 0) ^ (reduce(lambda x, y: x ^ y, nums2) if len(nums1) % 2 else 0)
        