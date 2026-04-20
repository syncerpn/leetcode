# easy
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        seats = [i for i, a in enumerate(seats) if a]
        ans = max(seats[0] - 0, n - 1 - seats[-1])
        for a, b in pairwise(seats):
            ans = max(ans, (b - a) // 2)
        return ans