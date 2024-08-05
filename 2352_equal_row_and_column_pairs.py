# tuple actually can be hashed, lol
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = {}
        for g in grid:
            t = tuple(g)
            if t not in d:
                d[t] = 0
            d[t] += 1
        ans = 0
        for g in zip(*grid):
            if g in d:
                ans += d[g]
        return ans

# trie solution
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        root = {}
        for g in grid:
            node = root
            for i in range(n):
                if i == n - 1:
                    if g[i] not in node:
                        node[g[i]] = 0
                    node[g[i]] += 1
                else:
                    if g[i] not in node:
                        node[g[i]] = {}
                    node = node[g[i]]
        ans = 0
        for g in zip(*grid):
            node = root
            for i in range(n):
                if g[i] not in node:
                    break
                if i == n - 1:
                    ans += node[g[i]]
                else:
                    node = node[g[i]]
        return ans