# fairly brute-force with optimized prefix sum impl
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        V = set(list("aeiou"))
        n = len(s)
        P = [0]
        for a in s:
            P.append(P[-1] + int(a in V))
        ans = 0
        for l in range(1, n // 2 + 1):
            if l * l % k != 0:
                continue
            v, c = 0, 0
            for i in range(2 * l, n + 1):
                if P[i] - P[i - 2 * l] == l:
                    ans += 1
        return ans

# but it is much better and clever
# to use prefix-sum and find the spot where number of vowels equals number of consonants
# then check for the length
# this is the only way to pass the higher-constraints #2949
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        kk = 1
        while kk * kk % (4 * k):
            kk += 1
        k = kk
        
        V = set(list("aeiou"))
        n = len(s)
        p = 0
        P = {0:{0:1}}
        ans = 0
        for i, a in enumerate(s):
            d = 1 if a in V else -1
            p += d
            if p not in P:
                P[p] = {}
            m = (i + 1) % k
            if m not in P[p]:
                P[p][m] = 0
            ans += P[p][m]
            P[p][m] += 1
        return ans