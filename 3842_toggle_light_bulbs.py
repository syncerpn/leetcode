# easy
class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        d = Counter(bulbs)
        return sorted([k for k in d if d[k] % 2])