# easy
class Solution:
    def smallestNumber(self, n: int) -> int:
        ans = 1
        while n:
            n >>= 1
            ans <<= 1
        
        return ans - 1