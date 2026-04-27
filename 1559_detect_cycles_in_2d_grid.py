# traversal solution
# can be solved with union-find as well
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def traverse(S):
            while S:
                c = S.pop()
                s = [(None, c)]
                v = set(c)
                while s:
                    p, c = s.pop()
                    x, y = c
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        q = (x + dx, y + dy)
                        if q not in S:
                            continue
                        if q == p:
                            continue
                        if q in v:
                            return True
                        v.add(q)
                        s.append((c, q))
                S -= v
            return False

        d = defaultdict(set)
        for i, row in enumerate(grid):
            for j, k in enumerate(row):
                d[k].add((i, j))
        
        for k in d:
            if traverse(d[k]):
                return True
        return False
        