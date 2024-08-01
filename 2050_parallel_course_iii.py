# topo sort + dynamic programming
# trying to find max time required for each course to start
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        degree = [0] * (n + 1)
        graph = {}
        order = []
        for x, y in relations:
            if x not in graph:
                graph[x] = []
            graph[x].append(y)
            degree[y] += 1
        q = deque([i for i in range(1, n+1) if degree[i] == 0])
        while q:
            x = q.popleft()
            order.append(x)
            if x in graph:
                for y in graph[x]:
                    degree[y] -= 1
                    if degree[y] == 0:
                        q.append(y)
        
        time = [0] + time
        prev = [0] * (n + 1)
        for x in order:
            if x in graph:
                for y in graph[x]:
                    prev[y] = max(prev[y], time[x] + prev[x])
            
        return max(t + p for t, p in zip(time, prev))