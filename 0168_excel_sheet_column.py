# modulo conversion
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber - 1
        r = ""
        while n >= 26:
            r = chr(n % 26 + 65) + r
            n = n // 26 - 1
        
        return chr(n % 26 + 65) + r