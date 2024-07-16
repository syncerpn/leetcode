# two pointer merging
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        r = []
        while i < len(nums1) and j < len(nums2):
            a, u = nums1[i]
            b, v = nums2[j]
            if a == b:
                r.append([a, u+v])
                i += 1
                j += 1
            elif a < b:
                r.append(nums1[i])
                i += 1
            else:
                r.append(nums2[j])
                j += 1
        
        if i < len(nums1):
            r += nums1[i:]
        if j < len(nums2):
            r += nums2[j:]
        return r