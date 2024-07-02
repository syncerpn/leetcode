# count and append
# to optimize a bit, try counting shorter array to save space (O(min(m, n)))
# and to answer follow-up question
# 1. What if the given array is already sorted? How would you optimize your algorithm?
# -> using two pointer should be fine
# 2. What if nums1's size is small compared to nums2's size? Which algorithm is better?
# -> below solution is find
# 3. What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
# -> split them into batch and process one batch at a time
# -> also a keyword to search: external sorting
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        d = {}
        r = []
        for n in nums1:
            if n not in d:
                d[n] = 0
            d[n] += 1
        
        for n in nums2:
            if n not in d:
                continue

            if d[n] <= 0:
                continue
            
            r.append(n)
            d[n] -= 1
    
        return r