# binary search
class Solution:
    def minimumK(self, nums: List[int]) -> int:
        def is_valid(k):
            return sum(a // k + int(a % k > 0) for a in nums) <= k * k
        
        l = 0
        r = sum(nums)
        while l < r - 1:
            m = (l + r) // 2
            if is_valid(m):
                r = m
            else:
                l = m
        
        return r