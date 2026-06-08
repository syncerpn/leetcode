# easy
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        return sum(int(c) for c in str(n))