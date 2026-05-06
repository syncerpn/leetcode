# two pointer
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        A = []
        B = []
        n = len(s)
        na = len(a)
        nb = len(b)
        for i in range(n-na+1):
            if s[i:i+na] == a:
                A.append(i)
        for i in range(n-nb+1):
            if s[i:i+nb] == b:
                B.append(i)
        
        ans = []
        i = 0
        for a in A:
            while i < len(B) and a - B[i] > k:
                i += 1
            if i < len(B) and k >= a - B[i] >= -k:
                ans.append(a)
        return ans
