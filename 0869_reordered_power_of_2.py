# hash sorted string
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        P = set(["".join(sorted(str(1 << i))) for i in range(32)])
        return "".join(sorted(str(n))) in P