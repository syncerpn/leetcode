# just verify each word with set of broken letters
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        bs = set(brokenLetters)
        words = text.split(" ")
        r = len(words)
        for word in words:
            for c in word:
                if c in bs:
                    r -= 1
                    break
        return r