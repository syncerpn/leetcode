# would you prefer string manip?
class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:]
        s = s[::-1] + "0" * (32-len(s))
        return int(s, 2)

# or bit manip?
class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        for _ in range(31):
            if n & 1:
                r = r | 1
            
            n = n >> 1
            r = r << 1
        
        return r | 1 if n & 1 else r