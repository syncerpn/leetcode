# good intro to priority queue
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        h = [-n for n in gifts]
        heapq.heapify(h)
        while k > 0:
            heapq.heappush(h, -int((-heapq.heappop(h)) ** 0.5))
            k -= 1
        
        return abs(sum(h))