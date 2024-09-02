# obviously heap
class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        h = []
        ans = []
        for x, y in queries:
            d = abs(x) + abs(y)
            heapq.heappush(h, -d)
            if len(h) < k:
                ans.append(-1)
            else:
                while len(h) > k:
                    heapq.heappop(h)
                t = heapq.heappop(h)
                ans.append(-t)
                heapq.heappush(h, t)
        return ans