# modified dijkstra algorithm
# we store the not one but two smallest times to reach each node
# the key point here is that we may revisit some nodes
# therefore the visited bitmask is not usuable
# we use bfs to find the shortest path each step
# and heap queue to keep searching from the shortest one so far
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        G = {}
        D = [[] for _ in range(n+1)]
        D[1] = [0]
        for a, b in edges:
            if a not in G:
                G[a] = []
            G[a].append(b)
            if b not in G:
                G[b] = []
            G[b].append(a)
        
        h = [(0, 1)]
        while h:
            l, a = heapq.heappop(h)
            if a == n and len(D[n]) == 2:
                break
            
            for b in G[a]:
                # green light red light
                # time calculation is also not easy
                if (l // change) % 2 == 0:
                    d = l + time
                else:
                    d = ceil(l / (2 * change)) * 2 * change + time
                
                # we store the shortest and second shortest time to reach b
                # no more than two
                # so D[b] should store at most 2
                # we only append when D[b] is empty
                # or when D[b] has only one shortest so far
                # and the second shortest should be different from the shortest one
                if not D[b] or (len(D[b]) == 1 and D[b] != [d]):
                    D[b] += [d]
                    heapq.heappush(h, (d, b))
        
        return max(D[n])