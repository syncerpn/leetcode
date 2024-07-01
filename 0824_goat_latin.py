# pure string manip
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        VOWELS = "AEIOUaeiou"
        words = sentence.split(" ")
        r = []
        for i, word in enumerate(words):
            if word[0] in VOWELS:
                r.append(word + "ma" + "a" * (i + 1))
            else:
                r.append(word[1:] + word[0] + "ma" + "a" * (i + 1))
        return " ".join(r)