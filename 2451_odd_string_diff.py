# easy, but pretty annoying
class Solution:
    def oddString(self, words: List[str]) -> str:
        def diff(word):
            d = []
            for a, b in pairwise(word):
                d.append(ord(b) - ord(a))
            return d
        
        x = diff(words[0])
        y = diff(words[1])
        z = diff(words[2])
        if x != y == z:
            return words[0]
        if x == z != y:
            return words[1]
        if x == y != z:
            return words[2]
        for a, b in pairwise(words[2:]):
            if diff(b) != diff(a):
                return b