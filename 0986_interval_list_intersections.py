# segment overlapping is familiar to me
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        m, n = len(firstList), len(secondList)
        i, j = 0, 0
        ans = []
        while i < m and j < n:
            a, b = firstList[i]
            x, y = secondList[j]
            p = max(a, x)
            q = min(b, y)
            if p <= q:
                ans.append([p, q])
            i += b == q
            j += y == q

        return ans