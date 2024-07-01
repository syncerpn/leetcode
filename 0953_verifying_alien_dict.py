# try sorting all
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        d = {}
        for a, o in zip(ALPHABET, order):
            d[o] = a
        return sorted(words, key=lambda w: "".join([d[c] for c in w])) == words

# or early stopping
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {c: i for i, c in enumerate(order)}
        def compare(wa, wb):
            i = 0
            while i < len(wa) and i < len(wb):
                if d[wa[i]] < d[wb[i]]:
                    return -1
                elif d[wa[i]] > d[wb[i]]:
                    return 1
                i += 1
            if len(wa) < len(wb):
                return -1
            elif len(wa) > len(wb):
                return 1
            return 0

        for wa, wb in pairwise(words):
            if compare(wa, wb) == 1:
                return False
        
        return True