# find its next power-of-two
class Solution:
    def findComplement(self, num: int) -> int:
        i = 1
        while i <= num:
            i *= 2
        
        return i - 1 - num