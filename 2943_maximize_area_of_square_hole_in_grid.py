# simply find the max gap between bars
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        ans = 1
        def max_gap(bars):
            g, ans = 2, 2
            for a, b in pairwise(bars):
                if b - a > 1:
                    g = 1
                g += 1
                ans = max(ans, g)
            return ans
        
        hmax, wmax = max_gap(sorted(hBars)), max_gap(sorted(vBars))
        gmax = min(hmax, wmax)
        return gmax * gmax