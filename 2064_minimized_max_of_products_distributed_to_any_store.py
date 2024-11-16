# fairly straight forward to binary search
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def is_valid(k):
            s = 0
            for q in quantities:
                s += q // k + ((q % k) > 0)
            return s <= n
        
        l = 1
        r = max(quantities)
        while l < r:
            m = (l + r) // 2
            if is_valid(m):
                r = m
            else:
                l = m + 1
        return r