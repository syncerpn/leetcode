# easy
# but requires math
class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        a, b, c = sides
        if abs(a - b) < c < a + b:
            return sorted([math.acos((i*i + j*j - k*k) / (2*i*j)) / math.pi * 180 for (i, j, k) in [(a, b, c), (b, c, a), (c, a, b)]])
        return []