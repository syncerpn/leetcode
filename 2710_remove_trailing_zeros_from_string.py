# track trailing zeros
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        i = 0
        while i < len(num):
            if num[i] != "0":
                break
            i += 1
        
        j = len(num) - 1
        while j >= 0:
            if num[j] != "0":
                break
            j -= 1
        
        return num[i:j+1]