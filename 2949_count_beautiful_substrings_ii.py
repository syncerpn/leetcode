# use prefix-sum and find the spot where number of vowels equals number of consonants
# then check for the length
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
        