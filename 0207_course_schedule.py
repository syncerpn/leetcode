# loop finding in graph
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            g[a].append(b)
        
        v = set()
        def dfs(a):
            if a in v:
                return False
            if not g[a]:
                return True

            v.add(a)
            for b in g[a]:
                if not dfs(b):
                    return False
            v.discard(a)
            g[a] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True