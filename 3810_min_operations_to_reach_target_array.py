# easy
class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        v = set(nums)
        ans = 0
        for a, t in zip(nums, target):
            if a in v and a != t:
                v.discard(a)
                ans += 1
        
        return ans