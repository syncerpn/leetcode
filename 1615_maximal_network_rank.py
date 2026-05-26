# O(n2) for pairing
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(set)
        for a, b in roads:
            d[a].add(b)
            d[b].add(a)
        ans = 0
        for a in range(n-1):
            for b in range(a+1, n):
                ans = max(ans, len(d[a]) + len(d[b]) - int(a in d[b]))
        return ans