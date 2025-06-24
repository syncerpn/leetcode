# fairly easy with hashmap
class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        xs, ys = {}, {}
        for x, y in coords:
            if x not in xs:
                xs[x] = (y, y)
            else:
                a, b = xs[x]
                xs[x] = (min(a, y), max(b, y))
            
            if y not in ys:
                ys[y] = (x, x)
            else:
                a, b = ys[y]
                ys[y] = (min(a, x), max(b, x))
        
        ans = 0
        
        mi, ma = min(xs.keys()), max(xs.keys())
        for x in xs:
            a, b = xs[x]
            ans = max(ans, (b - a) * (x - mi), (b - a) * (ma - x))

        mi, ma = min(ys.keys()), max(ys.keys())
        for y in ys:
            a, b = ys[y]
            ans = max(ans, (b - a) * (y - mi), (b - a) * (ma - y))
        return ans if ans else -1