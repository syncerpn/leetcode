# easy heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        h = [-n for n in nums]
        heapq.heapify(h)
        for _ in range(k):
            n = heapq.heappop(h)
            score += -n
            heapq.heappush(h, math.ceil(n // 3))
        return score