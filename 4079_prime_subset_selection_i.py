# sieve of course
# no precomputed
class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        P = [True] * (n + 1)
        P[0] = False
        P[1] = False
        ss = 0
        ans = []
        for i in range(2, n + 1):
            if not P[i]:
                continue
            ss += i
            if ss > s:
                break
            ans.append(i) 
            j = i
            while i * j < len(P):
                P[i * j] = False
                j += 1
        return ans

# with precomputed
P = [True] * 1000001
P[0] = False
P[1] = False
Q = []
S = [0]
for i in range(2, 1000001):
    if not P[i]:
        continue
    Q.append(i)
    S.append(S[-1] + i)
    j = i
    while i * j < len(P):
        P[i * j] = False
        j += 1

class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        i = bisect.bisect(S, s)
        j = bisect.bisect(Q, n)
        return Q[:min(i-1, j)]