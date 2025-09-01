# easy
class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        d = Counter([c for c in str(n)])
        a = sorted([(d[c], c) for c in d])
        return int(a[0][1])