# easy
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        d = {}
        for i, a in enumerate(nums):
            if a not in d:
                d[a] = []
            d[a].append(i)
        
        ans = []
        for i in queries:
            a = nums[i]
            if len(d[a]) == 1:
                ans.append(-1)
                continue
            j = bisect.bisect(d[a], i)
            t = inf
            if j == 1:
                t = min(d[a][j] - i, n - d[a][-1] + i)
            elif j == len(d[a]):
                t = min(i - d[a][j-2], n - i + d[a][0])
            else:
                t = min(d[a][j] - i, i - d[a][j-2])
            ans.append(t)
        return ans