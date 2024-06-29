# try to match/pair until the last char
# return true if exactly one char is left
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits)-1:
            if bits[i]:
                i += 2
            else:
                i += 1
        return i == len(bits)-1