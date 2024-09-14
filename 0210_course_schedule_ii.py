# topo sort of graph nodes
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            g[a].append(b)
        
        ans = []
        v, cycle = set(), set()
        def dfs(a):
            if a in cycle:
                return False
            if a in v:
                return True

            cycle.add(a)
            for b in g[a]:
                if not dfs(b):
                    return False
            
            cycle.discard(a)
            v.add(a)
            ans.append(a)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans
