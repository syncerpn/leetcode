# filter by k divisible first before checking all nums in nums2
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        c = 0
        for n1 in nums1:
            if n1 % k == 0:
                for n2 in nums2:
                    if n1 % (k * n2) == 0:
                        c += 1
        return c