# beated 99.34% with this pure condition checking solution, lol
class Solution:
    def countValidWords(self, sentence: str) -> int:
        DIGITS = "0123456789"
        MARKS = "!.,"

        words = [w for w in sentence.split(" ") if w != ""]

        r = 0
        for word in words:
            count_hyphen = 0
            n = len(word)
            for i,c in enumerate(word):
                if c in DIGITS:
                    break
                elif c == "-":
                    if i == 0 or i == n-1 or count_hyphen >= 1 or word[i+1] in MARKS:
                        break
                    count_hyphen += 1
                elif c in MARKS:
                    if i != n-1:
                        break
            else:
                r += 1
        return r