# straightforward
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        c = 0
        for p in patterns:
            c += p in word
        return c