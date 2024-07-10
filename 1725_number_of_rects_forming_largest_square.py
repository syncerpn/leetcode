# take min of sides of each rect to form square
# then count the number of max of square sides
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        sides = [min(rect) for rect in rectangles]
        return sides.count(max(sides))