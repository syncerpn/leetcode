# binary search at the first sight
# then also thought of reversed graph or trie
# but what surprised me most was that we dont even need to care about threshold
# the solution was just intended to test but then passed all, lol
# the logic is that, if we can reach all the nodes, we just need one edge to do that and so we can remove all others
# so the threshold is always satisfied as long as it is at least 1
# maybe a harder version of this problem should tie the threshold to some specific nodes
# but i dont know
# happy to solve this anyway lol
class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        g = {i: {} for i in range(n)}
        for a, b, w in edges:
            if a not in g[b]:
                g[b][a] = w
            g[b][a] = min(g[b][a], w)
        
        def is_valid(m):
            s = [0]
            v = set()
            while s:
                b = s.pop()
                if b not in v:
                    v.add(b)
                s += [a for a in g[b] if g[b][a] <= m and a not in v]
            return len(v) == n

        l = min([w for _, _, w in edges])
        r = max([w for _, _, w in edges])
        ans = -1
        while l <= r:
            m = (l + r) // 2
            if is_valid(m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans