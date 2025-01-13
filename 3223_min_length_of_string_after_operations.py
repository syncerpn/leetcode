# easy
# just count it
class Solution:
    def minimumLength(self, s: str) -> int:
        d = Counter(list(s))
        return sum(2 - (d[c] % 2) for c in d)

# oneliner
class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(2 - (v % 2) for _, v in Counter(list(s)).items())