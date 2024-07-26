# dijkstra algorithm
# with many little things that optimize the solution 10x time faster
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        g = {i: {} for i in range(n)}
        for a, b, d in edges:
            if d <= distanceThreshold:
                g[a][b] = d
                g[b][a] = d
        
        ans = 0
        c_min = n
        for i in range(n):
            # visited bitmask instead of set
            v = [False] * n
            # count it directly
            c = -1
            h = [(0, i)]

            # save shortest distance to a node to limit duplications in h
            distance = [float('inf')] * n
            distance[i] = 0

            while h:
                l, a = heapq.heappop(h)
                if v[a]:
                    continue
                v[a] = True
                c += 1
                for b in g[a]:
                    d = g[a][b]
                    # filtering out
                    if not v[b] and l + d <= distanceThreshold and l + d < distance[b]:
                        distance[b] = l + d
                        heapq.heappush(h, (l+d, b))

            if c_min >= c:
                c_min = c
                ans = i
        
        return ans