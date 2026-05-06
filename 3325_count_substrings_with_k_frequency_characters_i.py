# nice solution
# at this point, try to remember them
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ans = (n + 1) * n // 2
        count = Counter()
        i = 0
        for j in range(n):
            count[s[j]] += 1
            while count[s[j]] >= k:
                count[s[i]] -= 1
                i += 1
            ans -= j - i + 1
        return ans

# all diff
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        ans = 0
        l = 0
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
            while d[c] == k:
                d[s[l]] -= 1
                l += 1
            ans += l
        return ans