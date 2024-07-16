# just use set
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        s = set()
        for a, b in pairwise(nums):
            if (a + b) in s:
                return True
            s.add(a + b)
        return False