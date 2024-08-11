# easy
class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        x = 0
        y = 0
        for c in commands:
            if c == "RIGHT":
                y += 1
            if c == "LEFT":
                y -= 1
            if c == "UP":
                x -= 1
            if c == "DOWN":
                x += 1
        return x * n + y