# rolling max
# prefix sum
# fairly straightforward
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m = 0
        a = 0
        for g in gain:
            a += g
            m = max(m, a)
        return m