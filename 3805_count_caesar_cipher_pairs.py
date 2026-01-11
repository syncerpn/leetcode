# normalized tuples
class Solution:
    def countPairs(self, words: List[str]) -> int:
        A = {c: i for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        d = {}
        ans = 0
        for s in words:
            t = tuple((A[c] - A[s[0]]) % 26 for c in s)
            if t not in d:
                d[t] = 0
            d[t] += 1
            ans += d[t] - 1
        return ans