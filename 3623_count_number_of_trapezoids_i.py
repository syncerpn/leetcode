# fairly easy
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        d = {}
        for x, y in points:
            if y not in d:
                d[y] = 0
            d[y] += 1
        
        s, ans = 0, 0
        for y in d:
            d[y] = d[y] * (d[y] - 1) // 2
            ans = (ans + s * d[y]) % MOD
            s += d[y]
        
        return ans

# a bit faster implementation
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        d = Counter(y for x, y in points)
        
        s, ans = 0, 0
        for y in d:
            p = d[y] * (d[y] - 1) // 2
            ans = (ans + s * p) % MOD
            s = (s + p) % MOD
        
        return ans