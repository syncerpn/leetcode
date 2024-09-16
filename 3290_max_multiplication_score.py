# simple dp
# after understanding the concept
# this can be solved pretty much easily
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        CONSTRAINT_MIN = -(1 << 32)
        d = [CONSTRAINT_MIN for _ in range(4)]
        for bi in b:
            d[3] = max(d[3], d[2] + bi * a[3])
            d[2] = max(d[2], d[1] + bi * a[2])
            d[1] = max(d[1], d[0] + bi * a[1])
            d[0] = max(d[0], bi * a[0])
        return d[3]