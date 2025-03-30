# solved it myself
# the logic is not that difficult to think of
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        queries = sorted([(q, i) for i, q in enumerate(queries)])
        qi = 0
        ans = [0] * len(queries)

        m, n = len(grid), len(grid[0])
        h = [(grid[0][0], 0, 0)]
        grid[0][0] = 0

        t = 0

        while h:
            v, i, j = heapq.heappop(h)
            while qi < len(queries):
                q, k = queries[qi]
                if v < q:
                    break
                ans[k] = t
                qi += 1
            else:
                break
            
            t += 1

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= i + di < m and 0 <= j + dj < n and grid[i+di][j+dj] != 0:
                    heapq.heappush(h, (grid[i+di][j+dj], i+di, j+dj))
                    grid[i+di][j+dj] = 0

        else:
            while qi < len(queries):
                q, k = queries[qi]
                ans[k] = t
                qi += 1
        
        return ans

# cleaner implementation
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = [0] * len(queries)

        h = [(grid[0][0], 0, 0)]
        directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]
        grid[0][0] = 0
        t = 0

        for k, q in sorted(enumerate(queries), key=lambda x: x[1]):
            while h and h[0][0] < q:
                _, i, j = heappop(h)
                t += 1
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj]:
                        heappush(h, (grid[ni][nj], ni, nj))
                        grid[ni][nj] = 0
            ans[k] = t
        return ans