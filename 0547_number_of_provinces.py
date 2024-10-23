# union-find obviously
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        d = {i: i for i in range(n)}
        def find(x):
            while d[x] != x:
                x = d[x]
            return x
        
        for i, r in enumerate(isConnected):
            pi = find(i)
            for j, c in enumerate(r):
                pj = find(j)
                if c and pi != pj:
                    d[pj] = pi # not d[j] = pi; why i kept getting it wrong at this step??
                    
        s = set()
        for i in range(n):
            s.add(find(i))
        return len(s)