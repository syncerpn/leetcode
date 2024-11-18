# pretty much similar to the previous one #3355
# just use binary search to find the minimum k
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        def is_valid(k):
            changes = [0] * n
            for l, r, v in queries[:k]:
                changes[l] += v
                if r + 1 < n:
                    changes[r+1] -= v
        
            p = 0
            for a, b in zip(nums, changes):
                p += b
                if p < a:
                    print(p, k, a)
                    return False
            return True
        
        l = 0
        r = len(queries)
        ans = -1
        while l <= r:
            m = (l + r) // 2
            if is_valid(m):
                r = m - 1
                ans = m
            else:
                l = m + 1
        return ans