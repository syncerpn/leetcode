# too easy
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a, b = abs(x-z), abs(y-z)
        return 0 if a == b else (1 if a < b else 2)