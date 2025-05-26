# topo sort + dp
# not very clean solution but solved it myself with hints
# not that difficult to think of a solution anyway
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        A = "abcdefghijklmnopqrstuvwxyz"
        n = len(colors)
        g = [set() for _ in range(n)] # child nodes
        d = [0] * n # node degree
        for a, b in edges:
            g[a].add(b)
            d[b] += 1
        
        # we start from 0-degree nodes and keep going next
        root = [a for a in range(n) if d[a] == 0]
        
        dp = [{c: 0 for c in A} for _ in range(n)]

        v = set()

        ans = -1
        while root:
            v |= set(root)
            root_next = set()
            for a in root:
                dp[a][colors[a]] = dp[a][colors[a]] + 1
                for c in A:
                    ans = max(ans, dp[a][c])
                for b in g[a]:
                    if b in v:
                        return -1
                    d[b] -= 1
                    dp[b] = {c: max(dp[b][c], dp[a][c]) for c in A}
                    if d[b] == 0:
                        root_next.add(b)
            
            root = root_next

        if len(v) != n:
            return -1
        return ans