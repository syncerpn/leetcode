# line sweep
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        road = [0] * 1001
        for n, a, b in trips:
            road[a] += n
            road[b] -= n
        c = 0
        for a in road:
            c += a
            if c > capacity:
                return False
        return True