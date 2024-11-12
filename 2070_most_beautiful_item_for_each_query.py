# sorting and filtering + binary search
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: (x[0], -x[1]))
        s = []
        m = 0
        for i in items:
            if not s or (s[-1][0] != [0] and i[1] > m):
                m = i[1]
                s.append(i)
        ans = []
        for q in queries:
            t = bisect.bisect_right(s, q, key=lambda x: x[0])
            if t == 0:
                ans.append(0)
            else:
                ans.append(s[t-1][1])
        return ans