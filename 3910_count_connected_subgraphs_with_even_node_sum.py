# nothing fancy
# just bruteforce backtracking-like
# enumerate all subsets, check polarity and then connectivity
class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        def traverse(mask):
            r = []
            for a, f in enumerate(mask):
                if f:
                    r.append(a)
                    mask[a] = False
                    break
            while r:
                a = r.pop()
                for b in g[a]:
                    if mask[b]:
                        r.append(b)
                        mask[b] = False
            return not any(mask)

        n = len(nums)
        m = 1 << n
        g = {i: set() for i in range(n)}
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        
        ans = 0
        for i in range(1, m):
            mask = [False] * n
            p = 0
            for j in range(n):
                if (i & (1 << j)) != 0:
                    mask[j] = True
                    p += nums[j]
            if p % 2 == 0:
                ans += traverse(mask)
        return ans