# easy
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m = minutes * 6
        h = (hour % 12) * 30 + minutes / 60 * 30
        d = abs(m - h)
        return d if d <= 180 else 360 - d