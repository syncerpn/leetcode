# iterate backward should work
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        word_length = 0
        while i >= 0:
            if s[i] == " ":
                if word_length > 0:
                    return word_length
            else:
                word_length += 1
            i -= 1
        
        return word_length