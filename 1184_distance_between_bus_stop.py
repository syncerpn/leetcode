# array sum
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start == destination:
            return 0
        l = sum(distance)
        if start > destination:
            start, destination = destination, start
        f = sum(distance[start:destination])
        b = l - f
        return min(f, b)