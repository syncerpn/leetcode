# quite easy to understand if draw it out
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x11, y11, x12, y12 = rec1
        x21, y21, x22, y22 = rec2
        return x11 < x22 and x21 < x12 and y11 < y22 and y21 < y12