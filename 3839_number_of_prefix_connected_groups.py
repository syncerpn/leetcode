# easy
class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        d = Counter([w[:k] for w in words if len(w) >= k])
        return sum([d[i] > 1 for i in d])