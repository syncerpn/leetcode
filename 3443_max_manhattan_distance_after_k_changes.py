# very optimized solution
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        x, y = 0, 0
        for i, c in enumerate(s, 1):
            if c == "S":
                y += 1
            elif c == "N":
                y -= 1
            elif c == "E":
                x += 1
            elif c == "W":
                x -= 1
            d = abs(x) + abs(y) + 2 * k
            if d > i:
                d = i
            if d > ans:
                ans = d
        return ans