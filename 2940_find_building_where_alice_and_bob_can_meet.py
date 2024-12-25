# need revisit
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        def cmp(i, j):
            if i > j:
                return 1
            elif i < j:
                return -1
            return 0
        que = [[] for a in heights]
        h = []
        res = [-1] * len(queries)
        for qi, (i, j) in enumerate(queries):
            if cmp(i, j) == cmp(heights[i], heights[j]):
                res[qi] = max(i, j)
            else:
                que[max(i, j)].append([max(heights[i], heights[j]), qi])
        for i, a in enumerate(heights):
            while h and h[0][0] < a:
                res[heappop(h)[1]] = i
            for q in que[i]:
                heappush(h, q)
        return res
        