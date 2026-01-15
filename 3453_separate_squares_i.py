# binary search
# line sweep should be fine also
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        l, r, t = float('inf'), float('-inf'), 0

        for _, y, a in squares:
            t += a * a
            l = min(l, y)
            r = max(r, y + a)
        
        t = t / 2.0

        for i in range(60):
            m = (l + r) / 2.0

            tc = 0
            for _, y, a in squares:
                yc = max(0, min(a, m - y))
                tc += a * yc
            
            if tc < t:
                l = m
            else:
                r = m

        return m