# math should make it
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        s = mean * (n + m) - sum(rolls)
        t = s // n
        r = s - t * n
        if t < 1 or (t == 6 and r > 0) or t > 6:
            return []
        return [t] * (n - r) + [t+1] * r