# go forward or backward?
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        r = code[:]
        if k < 0:
            r[0] = sum(code[n+k:n])
            for i in range(1, n):
                r[i] = r[i-1] + code[i-1] - code[i+k-1]
        else:
            r[0] = sum(code[1:k+1])
            for i in range(1, n):
                r[i] = r[i-1] - code[i] + code[(i+k)%n]
        
        return r