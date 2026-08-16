# easy
class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        a, b = target
        ans = -1
        d_min = inf
        for i, (x, y, r) in enumerate(drones):
            d = abs(x - a) + abs(y - b)
            if d <= r and d < d_min:
                ans = i
                d_min = d
        return ans