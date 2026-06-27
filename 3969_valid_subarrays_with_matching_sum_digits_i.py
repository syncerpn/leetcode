# prefix sum digit pairing + binary search
class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        def f(a):
            while a >= 10:
                a //= 10
            return a
        
        n = len(nums)
        p = [0] * (n + 1)
        d = {k: [] for k in range(10)}
        d[0].append(0)
        for i, a in enumerate(nums):
            p[i+1] = p[i] + a
            d[p[i+1] % 10].append(i+1)
        
        ans = 0
        for a in range(10):
            b = (a + x) % 10
            
            for i in d[a]:
                k = bisect.bisect(d[b], i)
                for j in range(k, len(d[b])):
                    c = p[d[b][j]] - p[i]
                    if f(c) == x:
                        ans += 1
        return ans