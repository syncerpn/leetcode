# hash map
# or here, i used set
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        onces = set()
        mores = set()
        valids = set()

        for w in words1:
            if w in onces:
                mores.add(w)
            onces.add(w)
        
        for w in words2:
            if w in onces and w not in mores and w not in valids:
                valids.add(w)
            else:
                mores.add(w)
                valids.discard(w)
        
        return len(valids)
