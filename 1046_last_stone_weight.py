# pretty nice problem
# use heap queue to keep them in order
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for s in stones:
            heapq.heappush(h, -s)
        while len(h) > 1:
            a = heapq.heappop(h)
            b = heapq.heappop(h)
            if a != b:
                heapq.heappush(h, a - b)
        
        if h:
            return -h[0]
        return 0