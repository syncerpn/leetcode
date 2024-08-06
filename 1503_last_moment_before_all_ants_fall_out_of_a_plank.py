# think differently
# when two ants A and B meet, they change their directions
# it is the same as the two ants keep their directions, but change identity
# i.e. A now becomes B and B now becomes A
# therefore, time should be counted for the furthest ants
# left-moving ant position to the left end of the plank
# and right-moving ant position to the right end of the plank
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        m = 0
        if left:
            m = max(m, max(left))
        if right:
            m = max(m, n-min(right))
        return m