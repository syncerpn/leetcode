# nice prob
# got me thinking for quite a bit
# but in the end, we simply try to make tree that follows the rule
# by converting undirected edges to directed ones by checking their assigned colors
# this solution is when you need a graph
class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:
        g = {}
        n = len(colors)
        d = {"R": 2, "B": 1, "W": 0}
        R = set(list(range(n)))
        for a, b in edges:
            if (d[colors[a]] - d[colors[b]]) % 3 == 2:
                a, b = b, a
            elif (d[colors[a]] - d[colors[b]]) % 3 == 0:
                return -1
            if a not in g:
                g[a] = []
            g[a].append(b)
            if len(g[a]) > 2:
                return -1
            R.discard(b)
        R = list(R)
        return R[0] if len(R) == 1 else -1

# simpler one without graph
# just record each node's parent
# and make sure each node has at most 2 children
class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:
        n = len(colors)
        P = [-1] * n
        C = [ 0] * n
        d = {"R": 2, "B": 1, "W": 0}
        for a, b in edges:
            if (d[colors[a]] - d[colors[b]]) % 3 == 2:
                a, b = b, a
            elif (d[colors[a]] - d[colors[b]]) % 3 == 0:
                return -1
            if P[b] != -1 or C[a] == 2:
                return -1
            P[b] = a
            C[a] += 1
        return P.index(-1)