# i could solve it up to counting parallel lines
# yet failed to track the parallelograms
# this solution can do that by tracking mid point and midlines of the trapezoids
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        slopes = Counter()
        lines = Counter()
        mids = Counter()
        midlines = Counter()

        for (x1, y1), (x2, y2) in itertools.combinations(points, 2):
            dx, dy = x2 - x1, y2 - y1
            g = math.gcd(dx, dy)
            dx, dy = dx // g, dy // g
            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy

            inter = dx * y1 - dy * x1
            slopes[dx, dy] += 1
            lines[dx, dy, inter] += 1
            mids[x1 + x2, y1 + y2] += 1
            midlines[x1 + x2, y1 + y2, dx, dy, inter] += 1

        ans = sum(math.comb(v, 2) for v in slopes.values())
        ans -= sum(math.comb(v, 2) for v in lines.values())
        ans -= sum(math.comb(v, 2) for v in mids.values())
        ans += sum(math.comb(v, 2) for v in midlines.values())
        return ans