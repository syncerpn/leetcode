#1. starting from square root of area, going backward to 0
#2. until a factor is found
def solve(area: int) -> list:
    for i in range(int(area ** 0.5), 0, -1):
        if area % i == 0:
            return [area // i, i]