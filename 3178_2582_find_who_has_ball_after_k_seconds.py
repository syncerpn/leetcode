# one pass is of size n-1
# calculate number of pass and remainder to know the child index
class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        return n - 1 - k % (n - 1) if (k // (n - 1)) % 2 else k % (n - 1)