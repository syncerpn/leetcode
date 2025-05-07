# dijkstra
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        s = set([(0, 0)])
        t = 0
        h = [(0, 0, 0)]
        while h:
            t, x, y = heapq.heappop(h)
            if x == n - 1 and y == m - 1:
                break
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                u, v = x + dx, y + dy
                if 0 <= u < n and 0 <= v < m and (u, v) not in s:
                    heapq.heappush(h, (max(t, moveTime[u][v]) + 1, u, v))
                    s.add((u, v))
        
        return t