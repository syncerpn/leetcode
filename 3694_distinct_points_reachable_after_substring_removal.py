# prefix sum
class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        def move(c, x, y, r):
            if c == "L":
                x -= 1 * r
            elif c == "R":
                x += 1 * r
            elif c == "U":
                y += 1 * r
            elif c == "D":
                y -= 1 * r
            return x, y

        x, y = 0, 0
        for c in s:
            x, y = move(c, x, y, 1)
            
        d = set()
        dx, dy = 0, 0
        for i, c in enumerate(s):
            dx, dy = move(c, dx, dy, 1)
            if i >= k:
                dx, dy = move(s[i-k], dx, dy, -1)
            if i >= k - 1:
                d.add((x - dx, y - dy))
        
        return len(d)