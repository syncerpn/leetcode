# binary search + greedy check
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def is_valid(m):
            p = False
            s = 0
            for a in nums:
                if a <= m and not p:
                    s += 1
                    p = True
                else:
                    p = False
            return s >= k

        l, r = min(nums), max(nums)
        while l <= r:
            m = (l + r) // 2
            if is_valid(m):
                r = m - 1
            else:
                l = m + 1
        return r + 1