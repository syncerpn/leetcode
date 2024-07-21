# my initial solution with topological sort using dfs
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def visit(d, i, p, t, ans):
            if p[i]: return True
            if t[i]: return False
            
            t[i] = True
            if i in d:
                for j in d[i]:
                    if not visit(d, j, p, t, ans):
                        return False
            
            p[i] = True
            ans.append(i)
            return True
        
        def topological_sort(d, k):
            p = [False] * (k + 1)
            t = [False] * (k + 1)
            s = list(d.keys())
            ans = []
            for i in s:
                if not visit(d, i, p, t, ans):
                    return None
            
            return ans
            
        rows = {}
        for a, b in rowConditions:
            if a not in rows:
                rows[a] = []
            rows[a].append(b)
        
        rows_sorted = topological_sort(rows, k)
        if rows_sorted is None:
            return []
        
        cols = {}
        for l, r in colConditions:
            if l not in cols:
                cols[l] = []
            cols[l].append(r)
        
        cols_sorted = topological_sort(cols, k)
        if cols_sorted is None:
            return []
        
        rows_unused = set(list(range(1,k+1)))
        mat_x = {}
        for i, v in enumerate(rows_sorted[::-1]):
            mat_x[v] = [i, -1]
            rows_unused.discard(i)
        
        cols_unused = set(list(range(1,k+1)))
        for i, v in enumerate(cols_sorted[::-1]):
            if v not in mat_x:
                mat_x[v] = [-1, i]
            else:
                mat_x[v][1] = i
            cols_unused.discard(i)
        
        mat = [[0 for _ in range(k)] for _ in range(k)]
        for i in range(1, k+1):
            ri = -1
            ci = -1
            if i in mat_x:
                ri, ci = mat_x[i]
            if ri == -1:
                ri = rows_unused.pop()
            if ci == -1:
                ci = cols_unused.pop()
            mat[ri][ci] = i
        
        return mat

# more compact solution with degree of nodes and topo sort
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def generate_topological_sort(A):
            deg, graph, order = defaultdict(int), defaultdict(list), []
            for x, y in A:
                graph[x].append(y)
                deg[y] += 1
            q = deque([i for i in range(1, k + 1) if deg[i] == 0])
            while q:
                x = q.popleft()
                order.append(x)
                for y in graph[x]:
                    deg[y] -= 1
                    if deg[y] == 0: q.append(y)
            return order
        left_right_order = generate_topological_sort(colConditions)
        above_below_order = generate_topological_sort(rowConditions)
        if len(left_right_order) < k or len(above_below_order) < k: return []       
        m = {x: i for i, x in enumerate(left_right_order)}
        ans = [[0] * k for _ in range(k)]
        for i in range(k):
            ans[i][m[above_below_order[i]]] = above_below_order[i]
        return ans