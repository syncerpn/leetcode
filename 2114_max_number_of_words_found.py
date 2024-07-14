# count spaces instead
# O(1) space
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        r = 0
        for word in sentences:
            spaces = 0
            for c in word:
                if c == " ":
                    spaces += 1
            r = max(r, spaces+1)
        return r