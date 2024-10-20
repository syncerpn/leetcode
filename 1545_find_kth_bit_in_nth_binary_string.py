# fairly easy
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        inv = False
        if k == (1 << (n - 1)):
            return "1"
        elif k > (1 << (n - 1)):
            inv = True
            k = (1 << n) - k
        ans = self.findKthBit(n-1, k)
        return ans if not inv else str(1-int(ans))

# wtf??
# god level solution O(1) by lee
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return str(k // (k & -k) >> 1 & 1 ^ k & 1 ^ 1)