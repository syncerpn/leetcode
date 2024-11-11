# try to "interleave" n-1 and x
# all of the 0-bit in x should be replace with a bit from n-1
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        m = n - 1
        j = 0
        ans = 0
        while x > 0 or m > 0:
            d = x & 1
            e = m & 1
            ans = ans | ((d | e) << j)
            if not d:
                m >>= 1
            x >>= 1
            j += 1
        return ans