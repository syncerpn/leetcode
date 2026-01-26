# actually easy
# because it is a tree
# bfs to find distance from x to other nodes
# do similar thing with y and z as well
class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        g = {}
        for a, b in edges:
            if a not in g:
                g[a] = []
            g[a].append(b)
            if b not in g:
                g[b] = []
            g[b].append(a)
        
        def traverse(a):
            d = [0] * n
            l = 0
            v = [False] * n
            v[a] = True

            A = [a]
            while A:
                A_next = []
                for a in A:
                    d[a] = l
                    v[a] = True
                    for b in g[a]:
                        if v[b]:
                            continue
                        A_next.append(b)
                        
                l += 1
                A = A_next
            return d
        
        dx = traverse(x)
        dy = traverse(y)
        dz = traverse(z)
        ans = 0
        for da, db, dc in zip(dx, dy, dz):
            da, db, dc = sorted([da, db, dc])
            if da * da + db * db == dc * dc:
                ans += 1
        return ans