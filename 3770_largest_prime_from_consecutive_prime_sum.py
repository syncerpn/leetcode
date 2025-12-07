# a pre-built list of candidates will save you time
# but here, just assume we need to include that in the solution
# as well as a loose constraint if possible
# also learned a good trick to build the sieve of eratosthenes
class Solution:
    def largestPrime(self, n: int) -> int:
        p = [True] * (n + 1)
        p[0] = False
        p[1] = False
        ans = 0
        a = 2
        while a * a <= n:
            if p[a]:
                for i in range(a * a, n + 1, a):
                    p[i] = False
            a += 1
        s = 0
        for a in range(2, n + 1):
            if p[a]:
                if s + a > n:
                    break
                s += a
                if p[s]:
                    ans = s
        return ans