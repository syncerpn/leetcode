# easy
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = Counter(answers)
        return sum(d[k] // (k+1) * (k+1) + (k+1) * (d[k] % (k+1) > 0) for k in d)