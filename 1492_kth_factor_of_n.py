# O(sqrtn)
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        f = []
        t = int(n ** 0.5)
        for i in range(1, t + 1):
            if n % i == 0:
                f.append(i)
        
        if t * t == n:
            if k > 2 * len(f) - 1:
                return -1
            if k <= len(f):
                return f[k-1]
            return n // f[-(k-len(f)+1)]
        else:
            if k > 2 * len(f):
                return -1
            if k <= len(f):
                return f[k-1]
            return n // f[-(k-len(f))]