# nice one makes me rethink my first solution
class Solution:
    def minimumMaxValue(self, n: int, index: int, value: int) -> int:
        g = value
        for a in range(2, int(value ** 0.5) + 1):
            if value % a == 0:
                g = a
                break
        if (index == 0 and value <= 1) or (value - g - 2 * (index - 1) <= 1):
            return -1
        if index == n - 1:
            return value
        return value + g + 2 * (n - 2 - index)