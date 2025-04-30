# binary search solution
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        g = [0]
        for i, (a, b) in enumerate(pairwise(nums)):
            if b - a > maxDiff:
                g.append(i+1)
        
        ans = []
        for a, b in queries:
            if bisect.bisect(g, a) == bisect.bisect(g, b):
                ans.append(True)
            else:
                ans.append(False)

        return ans

# or union find
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        g = {0: 0}
        c = 0
        for i, (a, b) in enumerate(pairwise(nums)):
            if b - a > maxDiff:
                c += 1
            g[i+1] = c
        
        ans = []
        for a, b in queries:
            if g[a] == g[b]:
                ans.append(True)
            else:
                ans.append(False)

        return ans