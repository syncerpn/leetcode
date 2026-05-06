# easy
class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        n = len(possible)
        s = 2 * sum(possible) - n
        a = 0
        for i, p in enumerate(possible):
            if i == n - 1:
                break
            p = 2 * p - 1
            s -= p
            a += p
            if a > s:
                return i + 1
        return -1