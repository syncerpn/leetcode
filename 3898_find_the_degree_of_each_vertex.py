# easy
class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return [sum(g) for g in matrix]