# set tracking
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        banned = set()
        uncommon = set()
        for w in s1 + s2:
            if w not in uncommon and w not in banned:
                uncommon.add(w)
            else:
                banned.add(w)
                uncommon.discard(w)
        
        return uncommon