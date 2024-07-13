# bfs is barely enough for solving this problem
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        clusters = []
        for s, d in edges:
            i_merge_ref = None
            i = 0
            while i < len(clusters):
                c = clusters[i]
                if s in c or d in c:
                    if i_merge_ref is not None:
                        clusters[i_merge_ref] = clusters[i_merge_ref].union(c)
                        clusters.pop(i)
                        continue
                    else:
                        c.add(s)
                        c.add(d)
                        i_merge_ref = i
                i += 1
            
            if i_merge_ref is None:
                clusters.append(set([s, d]))
                
        for c in clusters:
            if source in c and destination in c:
                return True
        return False

# yet, union-find is just beautiful
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        UF = {}

        def find(x):
            if x not in UF:
                UF[x] = x
            
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            UF[root_x] = root_y

        for s, d in edges:
            union(s, d)
        
        return find(source) == find(destination)

# and even more optimized with union-find with size/rank (here is size version)
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        UF = {}
        SIZE = [1] * n

        def find(x):
            if x not in UF:
                UF[x] = x
            
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                size_x = SIZE[root_x]
                size_y = SIZE[root_y]
                if size_x < size_y:
                    UF[root_x] = root_y
                    SIZE[root_y] += SIZE[root_x]
                else:
                    UF[root_y] = root_x
                    SIZE[root_x] += SIZE[root_y]

        for s, d in edges:
            union(s, d)
        
        return find(source) == find(destination)