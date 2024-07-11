# fair simple
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        d = None
        r = -1
        for i, p in enumerate(points):
            a, b = p
            if a == x or y == b:
                di = abs(a - x) + abs(b - y)
                if d is None or di < d:
                    d = di
                    r = i
        
        return r
