# greedy assignment
# first, count the number of roads connected to each city
# then sort the values and assign greedily
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        d = {}
        for a, b in roads:
            if a not in d:
                d[a] = 0
            d[a] += 1

            if b not in d:
                d[b] = 0
            d[b] += 1
        
        r = 0
        cs = sorted(d.values())
        k = n + 1 - len(cs)
        for i, c in enumerate(cs):
            r += (i+k) * c
        return r