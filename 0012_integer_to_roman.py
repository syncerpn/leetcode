# scalable look up table
class Solution:
    def intToRoman(self, num: int) -> str:
        lut = {
            10   : {1: "I", 5: "V"},
            100  : {1: "X", 5: "L"},
            1000 : {1: "C", 5: "D"},
            10000: {1: "M"},
        }
        d = 10
        s = ""
        while num > 0:
            r = num % 10
            major = r // 5
            minor = r  % 5
            if minor == 4:
                if major:
                    s = lut[d*10][1] + s
                else:
                    s = lut[d][5] + s
                s = lut[d][1] + s
            else:
                s = minor * lut[d][1] + s
                if major:
                    s = lut[d][5] + s

            d *= 10
            num = num // 10
        
        return s