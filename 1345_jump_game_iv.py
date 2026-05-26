# bfs
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        d = {}
        for i, a in enumerate(arr):
            if a not in d:
                d[a] = []
            d[a].append(i)

        v = [True] * n
        v[0] = False
        s = deque([(0, 0)])
        
        while s:
            c, i = s.popleft()
            a = arr[i]
            if i == n - 1:
                return c
            if i > 0 and v[i-1]:
                s.append((c+1, i-1))
                v[i-1] = False
            if i < n - 1 and v[i+1]:
                s.append((c+1, i+1))
                v[i+1] = False
            if a in d:
                for j in d[a]:
                    if v[j]:
                        s.append((c+1, j))
                        v[j] = False
                del d[a]
        
        return -1