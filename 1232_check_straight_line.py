# math form
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        a, b = coordinates[0]
        c, d = coordinates[1]
        for e, f in coordinates[2:]:
            if (e - a) * (d - b) != (f - b) * (c - a):
                return False
        
        return True