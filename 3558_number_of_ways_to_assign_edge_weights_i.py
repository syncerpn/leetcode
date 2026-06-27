# just dfs to find the max path
# then apply math
# simply if the max path has n node
# it is similar to a n-bit number
# and we want to count the number of odd values
# should be 2 ** (n - 1)
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n = len(edges) + 1
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        def dfs(b, a):
            ans = 0
            for c in g[b]:
                if c != a:
                    ans = max(ans, dfs(c, b) + 1)
            return ans
        
        return pow(2, dfs(1, 0) - 1, MOD)