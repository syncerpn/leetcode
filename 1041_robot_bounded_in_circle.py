# simulate 4 times
# actually the proof why 4 times are enough is a bit more complicated
# good problem for math
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        instructions *= 4
        D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = 0
        x, y = 0, 0
        for c in instructions:
            if c == "G":
                a, b = D[i]
                x += a
                y += b
            elif c == "L":
                i = (i - 1) % 4
            else:
                i = (i + 1) % 4
        return x == 0 and y == 0

# simplify into direction checking
# if after 1 time, the direction changes, we can guarantee a coming back to the original position
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = 0
        x, y = 0, 0
        for c in instructions:
            if c == "G":
                a, b = D[i]
                x += a
                y += b
            elif c == "L":
                i = (i - 1) % 4
            else:
                i = (i + 1) % 4
        return (x == 0 and y == 0) or i != 0