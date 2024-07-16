# iterate pair from left to right
# swap the first pair found if the second digit is smaller than the first one of the pair
class Solution:
    def getSmallestString(self, s: str) -> str:
        for i in range(len(s)-1):
            a = int(s[i])
            b = int(s[i+1])
            if b % 2 == a % 2 and b < a:
                return s[:i] + s[i+1] + s[i] + s[i+2:]
        
        return s