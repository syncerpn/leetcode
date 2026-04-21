# union-find
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        p = [i for i in range(n)]
        r = [0 for _ in range(n)]
        def find(x):
            while x != p[x]:
                x = p[x]
            return x
        
        def union(x, y):
            px = find(x)
            py = find(y)
            if r[px] > r[py]:
                p[py] = px
                r[px] += 1
            else:
                p[px] = py
                r[py] += 1
        
        for a, b in allowedSwaps:
            union(a, b)

        s, t = defaultdict(lambda: defaultdict(int)), defaultdict(lambda: defaultdict(int))
        for i in range(n):
            pi = find(i)
            si = source[i]
            ti = target[i]
            s[pi][si] += 1
            t[pi][ti] += 1
        ans = 0
        for pi in s:
            for si in s[pi]:
                ans += max(0, s[pi][si] - t[pi][si])
        return ans