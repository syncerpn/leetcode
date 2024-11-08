# also fairly easy
# just group them by the number of set bits
# then find min and max of the group
# while checking whether the max of a group is followed by a min of the next one
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def nset(x):
            n = 0
            while x > 0:
                n += x & 1
                x >>= 1
            return n
        
        p, l, r, m = nset(nums[0]), nums[0], nums[0], -1
        for n in nums[1:]:
            q = nset(n)
            if q == p:
                l = min(l, n)
                r = max(r, n)
            else:
                if l < m:
                    return False
                p, l, r, m = q, n, n, r
        if l < m:
            return False
        return True