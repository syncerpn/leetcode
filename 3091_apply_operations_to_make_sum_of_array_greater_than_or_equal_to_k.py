# math
class Solution:
    def minOperations(self, k: int) -> int:
        q = int(k ** 0.5)
        m = int(math.ceil(k / q))
        return q + m - 2