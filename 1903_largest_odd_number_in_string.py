# go backward, checking for the first odd number
# return all number from the beginning until that one
# because it should contain the most number of digits
class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num) - 1
        while i >= 0:
            if int(num[i]) % 2:
                return num[:i+1]
            i -= 1
        
        return ""
