# precomputed sieve
# not so beautiful
# just pure/straight forward logic
# that somehow still works lol
P = [True] * 1001
P[0] = False
P[1] = False
Q = []
for i in range(2, 1001):
    if not P[i]:
        continue
    Q.append(i)
    j = i
    while i * j < len(P):
        P[i * j] = False
        j += 1

class Solution:
    def maxPrimeSubset(self, n: int, s: int) -> list[int]:
        m = len(Q)
        d = {}
        for q in Q:
            if q > min(s, n):
                break
            S = sorted(list(d.keys()), reverse=True)
            for p in S:
                ss = p + q
                if ss > s:
                    continue
                pq = d[p] + [q]
                if ss not in d:
                    d[ss] = pq
                elif len(d[ss]) > len(pq):
                    d[ss] = pq
                elif len(d[ss]) == len(pq):
                    for a, b in zip(d[ss], pq):
                        if a > b:
                            d[ss] = pq
                            break
                        if a < b:
                            break
            d[q] = [q]
        if not d:
            return []
        k = max(d.keys())
        return d[k]