# count each char
# and the numbers of each char should be divisible by number of words
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        d = {}
        for word in words:
            for c in word:
                if c not in d:
                    d[c] = 0
                d[c] += 1
        
        for k in d:
            if d[k] % n != 0:
                return False
        return True