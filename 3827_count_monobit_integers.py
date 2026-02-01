# easy
class Solution:
    def countMonobit(self, n: int) -> int:
        ans = 1
        t = 1
        while t <= n:
            ans += 1
            t = (t << 1) + 1
        return ans

# bit-length
class Solution:
    def countMonobit(self, n: int) -> int:
        return (n + 1).bit_length()