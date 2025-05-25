# easy
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = {}
        ans = 0
        for s in words:
            a, b = s
            r = b + a
            if r in d:
                d[r] -= 1
                ans += 4
                if d[r] == 0:
                    del d[r]
            else:
                if s not in d:
                    d[s] = 0
                d[s] += 1
        
        for s in d:
            a, b = s
            if a == b:
                ans += 2
                break
        return ans