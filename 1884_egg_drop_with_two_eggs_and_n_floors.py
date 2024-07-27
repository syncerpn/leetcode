# strategy is always drop egg at floor n, n-1, n-2, n-3, and so on.
class Solution:
    def twoEggDrop(self, n: int) -> int:
        i, s = 0, 0
        while s < n:
            s += i
            i += 1
        return i-1

# or math
class Solution:
    def twoEggDrop(self, n: int) -> int:
        return round((n * 2) ** 0.5)