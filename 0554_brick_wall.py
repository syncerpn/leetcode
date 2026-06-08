# easy
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d = {}
        n = len(wall)
        for w in wall:
            p = 0
            for a in w[:-1]:
                p += a
                if p not in d:
                    d[p] = 0
                d[p] += 1
        if not d:
            return n
        return n - max(list(d.values()))