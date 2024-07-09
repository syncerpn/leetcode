# actually, we just need to care about start and end points
# there are two cases
# 1. not passing the starting point in the last round
# 2. or passed the starting point in the last round
# answer depends on these
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        s = rounds[0]
        e = rounds[-1]
        return list(range(1, e + 1)) + list(range(s, n+1)) if e < s else list(range(s, e+1))
