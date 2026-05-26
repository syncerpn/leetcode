# without inverse pow
# binary search is the way
class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        def kth_root(a):
            if a < 2:
                return a
            l, r = 1, a
            while l <= r:
                m = (l + r) // 2
                if m ** k < a:
                    l = m + 1
                else:
                    r = m - 1
            return l
        
        p, q = kth_root(l), kth_root(r)
        return q - p + int(q ** k == r)
