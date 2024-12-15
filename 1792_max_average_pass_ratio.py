# maximize average increment
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = [[a/b - (a+1)/(b+1), a, b] for a, b in classes]
        heapq.heapify(h)
        for _ in range(extraStudents):
            r, a, b = heapq.heappop(h)
            a += 1
            b += 1
            heapq.heappush(h, [a/b - (a+1)/(b+1), a, b])
        return sum([a/b for _, a, b in h]) / len(h)
