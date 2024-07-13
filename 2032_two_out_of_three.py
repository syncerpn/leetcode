# pure set intersection and union
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        r = s1.intersection(s2)
        s1 = s1.union(s2)
        s3 = set(nums3)
        r = r.union(s1.intersection(s3))
        return list(r)