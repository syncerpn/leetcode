# no actual pow or big number
# simply mod and state
# good problem anyway
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        d = {}
        for a in range(10):
            j, b = 1, a
            d[a] = {}
            v = set()
            while b not in v:
                v.add(b)
                d[a][j] = b
                b = (b * a) % 10
                j += 1
        ans = []
        for i, (a, b, c, m) in enumerate(variables):
            a = a % 10
            b = (b - 1) % len(d[a]) + 1
            k = d[a][b]
            p = 1
            v = set()
            s = []
            for _ in range(c):
                p = (p * k) % m
                if p == 0:
                    break
                if p in v:
                    p = s[(c - 1) % len(s)]
                    break
                v.add(p)
                s.append(p)

            if p == target:
                ans.append(i)
        return ans