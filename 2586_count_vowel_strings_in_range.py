# just count
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        VOWELS = "aeiou"
        c = 0
        for i in range(left, right+1):
            if words[i][0] in VOWELS and words[i][-1] in VOWELS:
                c += 1
        
        return c