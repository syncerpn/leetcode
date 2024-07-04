# good problem, for practicing binary search
# again, solution is easy to validate, yet finding a strategy is not trivial
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def is_valid(m):
            s = 0
            ki = k
            for i in range(len(nums)):
                n = nums[i]
                if s + n > m:
                    ki -= 1
                    s = 0
                    if k == 0:
                        return False
                s += n
            ki -= 1
            return ki >= 0
        
        l = max(nums)
        r = sum(nums)
        while l < r:
            m = (l + r) // 2
            if is_valid(m):
                r = m
            else:
                l = m + 1
        return r