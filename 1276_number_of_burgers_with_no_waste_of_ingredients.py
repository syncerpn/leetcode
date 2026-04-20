# easy
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        a = tomatoSlices - 2 * cheeseSlices
        if a < 0 or a % 2:
            return []
        a //= 2
        if a > cheeseSlices:
            return []
        return [a, cheeseSlices - a]