# starting from square root of area, going backward to 0
# until a factor is found
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(area ** 0.5), 0, -1):
            if area % i == 0:
                return [area // i, i]