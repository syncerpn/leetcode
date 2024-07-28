# just care about index 1
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        if n == 2:
            return 1
        i = 2
        c = 1
        while i != 1:
            i <<= 1
            if i >= n:
                i -= n - 1
            c += 1
        return c