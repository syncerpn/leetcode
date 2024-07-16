# if there are common digits, take the smallest one
# if there are none, take smallest of each, then form the number
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s = set(nums1).intersection(set(nums2))
        if s:
            return min(s)
        a = min(nums1)
        b = min(nums2)
        return min(a, b) * 10 + max(a, b)