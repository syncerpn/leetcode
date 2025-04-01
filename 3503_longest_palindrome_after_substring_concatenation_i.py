# brute-force solution
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        ans = 1
        m, n = len(s), len(t)
        for sl in range(m):
            for sr in range(sl, m+1):
                for tl in range(n):
                    for tr in range(tl, n+1):
                        v = s[sl:sr] + t[tl:tr]
                        if v == v[::-1]:
                            ans = max(ans, len(v))
        
        return ans