# counting with hash table, or maybe use sorting
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ds = []
        for word in words:
            d = {}
            for c in word:
                if c not in d:
                    d[c] = 0
                d[c] += 1
            ds.append(d)
        
        s = [words[0]]
        r = [ds[0]]
        for i in range(1, len(words)):
            if ds[i] != r[-1]:
                r.append(ds[i])
                s.append(words[i])
        
        return s