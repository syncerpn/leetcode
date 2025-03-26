# interval merging
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        h = sorted((sx, ex) for sx, _, ex, _ in rectangles)
        c = 1
        s, e = h[0]
        for a, b in h[1:]:
            if a >= e:
                c += 1
                if c > 2:
                    return True
                s = a
            e = max(b, e)

        h = sorted((sy, ey) for _, sy, _, ey in rectangles)
        c = 1
        s, e = h[0]
        for a, b in h[1:]:
            if a >= e:
                c += 1
                if c > 2:
                    return True
                s = a
            e = max(b, e)

        return False