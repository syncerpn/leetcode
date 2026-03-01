# easy
class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        V = {"a", "e", "i", "o", "u"}
        r = len(s) - 1
        while r >= 0:
            if s[r] not in V:
                break
            r -= 1
            
        
        return s[:r+1]