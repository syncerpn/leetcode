# easy
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        r = []
        for i, word in enumerate(words):
            if x in word:
                r.append(i)
        return r