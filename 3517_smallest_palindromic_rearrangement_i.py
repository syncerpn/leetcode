# fairly easy
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        m = s[n//2] if n % 2 else ""
        d = Counter(s)
        ans = ""
        for k in sorted(d.keys()):
            ans += k * (d[k] // 2)
        
        return ans + m + ans[::-1]