# easy
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word) // k
        d = Counter(list([word[i*k:i*k+k] for i in range(n)]))
        return n - max(d.values())