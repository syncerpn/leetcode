# counting again
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charset = {}
        for c in chars:
            if c not in charset:
                charset[c] = 0
            charset[c] += 1
        
        r = 0
        for word in words:
            wordchar = {}
            for c in word:
                if c not in charset:
                    break
                if c not in wordchar:
                    wordchar[c] = 0
                wordchar[c] += 1
                if wordchar[c] > charset[c]:
                    break
            else:
                r += len(word)
        
        return r