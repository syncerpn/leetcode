# merge
# two pointer
class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        i, j = 0, 0
        m, n = len(series1), len(series2)
        series1.append((inf, 0))
        series2.append((inf, 0))
        ans = []
        while i < m and j < n:
            a, u = series1[i]
            b, v = series2[j]
            if a < b:
                ans.append((a, u + v))
                i += 1
            elif a > b:
                ans.append((b, u + v))
                j += 1
            else:
                ans.append((a, u + v))
                i += 1
                j += 1
        
        while i < m:
            ans.append(series1[i])
            i += 1
            
        while j < n:
            ans.append(series2[j])
            j += 1

        return ans