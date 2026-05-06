# same idea as previous version
# but because of the higher constraints
# we need a better string matching algo
# that is kmp
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def kmp(s):
           dp = [0] * len(s)
           for i in range(1, len(s)):
               cur = dp[i - 1]
               while cur and s[i] != s[cur]:
                   cur = dp[cur - 1]
               dp[i] = cur + (s[i] == s[cur])
           return dp
           
        n = len(s)
        na = len(a)
        nb = len(b)

        va = kmp(a + '#' + s)
        vb = kmp(b + '#' + s)
        A = [i - na - na for i,v in enumerate(va) if v >= na]
        B = [i - nb - nb for i,v in enumerate(vb) if v >= nb]
        
        ans = []
        i = 0
        for a in A:
            while i < len(B) and a - B[i] > k:
                i += 1
            if i < len(B) and k >= a - B[i] >= -k:
                ans.append(a)
        return ans

        