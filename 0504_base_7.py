# string concat and modulo
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num < 0:
            return "-" + self.convertToBase7(abs(num))
        if num == 0:
            return "0"
        r = ""
        while num:
            r = str(num % 7) + r
            num = num // 7
        
        return str(r)