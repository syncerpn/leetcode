# easy
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        c1, c2 = nums1.count(0), nums2.count(0)
        if c1 == 0 and c2 == 0:
            return s1 if s1 == s2 else -1
        if c1 == 0:
            return s1 if s2 + c2 <= s1 else -1
        if c2 == 0:
            return s2 if s1 + c1 <= s2 else -1
        return max(s1+c1, s2+c2)
        
