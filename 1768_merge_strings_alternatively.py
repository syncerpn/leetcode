# fairly simple
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        r = ""
        while i < len(word1) and i < len(word2):
            r += word1[i] + word2[i]
            i += 1
        
        if i < len(word1):
            r += word1[i:]
        else:
            r += word2[i:]
        return r