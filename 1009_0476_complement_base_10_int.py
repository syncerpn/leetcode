# try using pure bit manip
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        k = 1
        m = n
        while m > 1:
            m >>= 1
            k = (k << 1) | 1
        return k ^ n