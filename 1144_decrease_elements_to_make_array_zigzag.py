# easy 2 cases
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        o = 0
        for i in range(0, n, 2):
            a = nums[i]
            v = a
            if i > 0:
                v = min(nums[i-1] - 1, v)
            if i < n - 1:
                v = min(nums[i+1] - 1, v)
            o += a - v
        
        e = 0
        for i in range(1, n, 2):
            a = nums[i]
            v = a
            if i > 0:
                v = min(nums[i-1] - 1, v)
            if i < n - 1:
                v = min(nums[i+1] - 1, v)
            e += a - v
        return min(o, e)