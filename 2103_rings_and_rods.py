# just check
class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [[False, False, False] for i in range(10)]
        COLORS = {"R":0, "G":1, "B":2}
        for i in range(0, len(rings), 2):
            c = rings[i]
            r = rings[i+1]
            rods[int(r)][COLORS[c]] = True
        return sum([all(r) for r in rods])