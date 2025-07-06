# easy
class Solution:
    def concatHex36(self, n: int) -> str:
        A = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = ""
        p = n * n * n
        while p > 0:
            ans = A[p % 36] + ans
            p //= 36
        
        p = n * n
        while p > 0:
            ans = A[p % 16] + ans
            p //= 16
        
        return ans