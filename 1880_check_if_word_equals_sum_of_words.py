# calculate the sum and compare
# be awared of this case: "aaaa" = 0000 = 0
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        ALPHABET = "abcdefghij"
        d = {c: i for i, c in enumerate(ALPHABET)}
        def get_value(s):
            v = 0
            for c in s:
                v = v * 10 + d[c]
            return v
            
        return get_value(firstWord) + get_value(secondWord) == get_value(targetWord)