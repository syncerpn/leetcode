# you can compare character
# i mean not just equal but also greater and smaller
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        i = 0
        m = ""
        while i < n-2:
            if num[i+2] != num[i+1]:
                i += 1
            elif num[i+2] == num[i+1] and num[i+1] == num[i]:
                m = max(m, num[i:i+3])            
            i += 1
            
        return m