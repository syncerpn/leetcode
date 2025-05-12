# easy
class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        d = Counter(s)
        v = sorted(d.values())
        return sum(v[0:max(0, len(v)-k)])