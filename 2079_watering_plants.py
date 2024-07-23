# fairly good array problem
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        steps = 0
        p = 0
        for i in range(n):
            if plants[i] + p <= capacity:
                p += plants[i]
            else:
                p = plants[i]
                steps += i * 2

        return steps + n