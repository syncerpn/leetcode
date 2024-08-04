# dijkstra everytime
# pretty slow but still pass
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def bfs():
            h = [(0, 0)]            
            v = [False] * n
            while h:
                a, d = heapq.heappop(h)
                if a == n-1:
                    return d
                if v[a]:
                    continue
                v[a] = True
                for b in g[a]:
                    if not v[b]:
                        heapq.heappush(h, (b, d+1))
            return 0


        g = {a: [b] for a, b in pairwise(list(range(n)))}
        ans = []
        for a, b in queries:
            g[a].append(b)
            ans.append(bfs())

        return ans

# much faster with distance array dp
# retro update the shortest distance as we have a new road each query
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g = [[i+1] for i in range(n-1)] + [[]]
        d = [i for i in range(n)]
        ans = []
        
        for i, j in queries:
            g[i].append(j)
            
            if d[i] + 1 < d[j]:
                q = [j]
                d[j] = d[i] + 1
                
                # update shortest distance to previous nodes leading to j
                while q:
                    v = q[0]
                    q = q[1:]
                    
                    for k in g[v]:
                        if d[v] + 1 < d[k]:
                            d[k] = d[v] + 1
                            q.append(k)
            
            ans.append(d[-1])
        
        return ans