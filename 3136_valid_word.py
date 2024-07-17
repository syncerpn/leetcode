# pure conditions checking
class Solution:
    def isValid(self, word: str) -> bool:
        VOWELS = "aeiouAEIOU"
        DIGITS = "1234567890"
        if len(word) < 3:
            return False
        has_vowel = False
        has_consn = False
        for c in word:
            if c in VOWELS:
                has_vowel = True
            elif "a" <= c <= "z" or "A" <= c <= "Z":
                has_consn = True
            elif c not in DIGITS:
                return False
        return has_vowel and has_consn
            