# dp/backtrack
class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        def generate(i, kk):
            if kk < i or i == n:
                return [0]
            
            if i == n - 1:
                return [0, 1]
            
            ss = []
            s = generate(i + 2, kk - i)
            for a in s:
                ss.append((2 << (n - 2 - i)) | a)
            
            ss += generate(i + 1, kk)
            return ss
        ss = generate(0, k)
        ans = []
        for a in ss:
            b = bin(a)[2:]
            l = len(b)
            ans.append((n - l) * "0" + b)
        return ans