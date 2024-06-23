# count and compare two dicts key lists and value lists
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        d1 = {}
        d2 = {}
        for c1, c2 in zip(word1, word2):
            if c1 not in d1:
                d1[c1] = 0
            d1[c1] += 1

            if c2 not in d2:
                d2[c2] = 0
            d2[c2] += 1
        
        return sorted(d1.keys()) == sorted(d2.keys()) and sorted(d1.values()) == sorted(d2.values())
