# prime again
class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        P = [False] * (n + 1)
        for a in range(2, int(n ** 0.5) + 1):
            if P[a]:
                continue
            b = a * a
            while b <= n:
                P[b] = True
                b += a
        
        ans = []
        for a in range(2, n // 2 + 1):
            if P[a]:
                continue
            if P[n-a]:
                continue
            ans.append((a, n-a))
        return ans

# better runtime with pre-cached list of primes