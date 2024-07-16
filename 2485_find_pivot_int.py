# why use other ways if we can use math in O(1)
class Solution:
    def pivotInteger(self, n: int) -> int:
        x = ((n * n + n) / 2) ** 0.5
        return int(x) if x == int(x) else -1