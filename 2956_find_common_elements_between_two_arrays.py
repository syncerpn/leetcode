# hash table
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1, c2 = 0, 0
        d1, d2 = {}, {}
        for n in nums1:
            d1[n] = 1 if n not in d1 else d1[n] + 1

        for n in nums2:
            d2[n] = 1 if n not in d2 else d2[n] + 1

        for n in d1:
            if n in d2:
                c1 += d1[n]
                
        for n in d2:
            if n in d1:
                c2 += d2[n]
        
        return [c1, c2]