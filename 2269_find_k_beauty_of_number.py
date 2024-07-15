# sliding window checking
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        n = len(s)
        c = 0
        for i in range(n-k+1):
            d = int(s[i:i+k])
            if d != 0 and num % d == 0:
                c += 1
        return c