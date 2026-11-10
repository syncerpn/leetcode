# need two heaps
# free and busy
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n = len(servers)
        m = len(tasks)
        h = []
        f = []
        for i, a in enumerate(servers):
            heapq.heappush(f, (a, i))
        
        ans = [-1] * m
        for j, t in enumerate(tasks):
            while h and h[0][0] <= j:
                c, a, i = heapq.heappop(h)
                heapq.heappush(f, (a, i))
            
            c = j
            if not f:
                c, a, i = heapq.heappop(h)
            else:
                a, i = heapq.heappop(f)
            ans[j] = i
            heapq.heappush(h, (c+t, a, i))
        return ans