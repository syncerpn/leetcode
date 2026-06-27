# line sweep
class Solution:
    def minLights(self, lights: list[int]) -> int:
        n = len(lights)
        s = [0] * (n + 1)
        for i, a in enumerate(lights):
            if a > 0:
                s[max(0, i - a)] += 1
                s[min(n, i + a + 1)] -= 1
        
        p, q = 0, 0
        ans = 0
        for i in range(n):
            p += s[i]
            if p == 0:
                q += 1
            else:
                ans += q // 3 + (1 if q % 3 else 0)
                q = 0
        
        ans += q // 3 + (1 if q % 3 else 0)
        return ans