# actually easier to think of a solution that #3243
# yet i failed to implement it
# we may use sortedlist or sortedset
# or just native dict like this, and still passed
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        d = {i:i+1 for i in range(n-1)}

        for a, b in queries:
            if a in d and d[a] < b:
                i = d[a]
                while i < b:
                    i = d.pop(i)
                d[a] = b
            ans.append(len(d))
        return ans