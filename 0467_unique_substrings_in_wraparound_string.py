# find the candidate substrings is quite easy
# just by check for increasing character sequence
# we need a way to deal with duplications
# one way is to count substrings starting with each char
# as follows
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        A = "abcdefghijklmnopqrstuvwxyz"
        d = {a: i for i, a in enumerate(A)}
        q = [0] * 26
        p, k = s[0], 1
        for c in s:
            if d[c] == (d[p] + k) % 26:
                k += 1
            else:
                p = c
                k = 1
            q[d[p]] = max(q[d[p]], k)
        qq = [0] * 26
        ans = 0
        for i in range(26):
            for j in range(26):
                qq[i] = max(qq[i], q[(i-j)%26]-j)
            ans += qq[i]
        return ans

# lee's solution is just crazily concise
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        res = {i: 1 for i in s}
        l = 1
        for i, j in zip(s, s[1:]):
            l = l + 1 if (ord(j) - ord(i)) % 26 == 1 else 1
            res[j] = max(res[j], l)
        return sum(res.values())