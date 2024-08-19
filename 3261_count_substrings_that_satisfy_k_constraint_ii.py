# we need to pre-compute all substrings that satisfy the constraints first
# then do query
# prefix sum + early stopping to reduce processing time
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        l = 0
        ones, zeros = 0, 0
        p, a = [0] * n, [0] * n
        t = 0
        for i in range(n):
            if s[i] == "0":
                zeros += 1
            else:
                ones += 1
            while zeros > k and ones > k:
                if s[l] == "0":
                    zeros -= 1
                else:
                    ones -= 1
                l += 1
        
            p[i] = i - l + 1
            t += p[i]
            a[i] = t
        
        ans = []
        for l, r in queries:
            c = 0
            for i in range(l, r+1):
                m = i - l + 1
                if p[i] <= m:
                    if i > 0:
                        c += a[r] - a[i-1]
                    else:
                        c += a[r]
                    break
                else:
                    c += m
            
            ans.append(c)
        return ans